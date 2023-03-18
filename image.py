import fitz
import PIL.Image
import io

pdf = fitz.open("sample1.pdf")
counter = 1
for i in range(len(pdf)):    #iterate over each page in pdf
    page = pdf[i]
    images = page.get_images()
