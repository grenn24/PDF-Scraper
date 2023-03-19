import fitz
import PIL.Image
import io

pdf = fitz.open("sample1.pdf")
counter = 1
for i in range(len(pdf)):    #iterate over each page in pdf
    page = pdf[i]
    images = page.get_images()
    for image in images:     #iterate over each extracted image
        base_img = pdf.extract_image(image[0])
        print(base_img)     #extract image metadata
        image_data = base_img["image"]     #extract image data
        img = PIL.Image.open(io.BytesIO(image_data))     #process image data
        ext = base_img["ext"]     #extract image extension
        img.save(open(f"image{counter}.{ext}", "wb"))     #save image as readable file
        counter += 1     #repeat for subsequent images