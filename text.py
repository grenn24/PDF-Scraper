import re
from pdfminer.high_level import extract_pages, extract_text

#extract all text from pdf file
text = extract_text("sample1.pdf")
print(text)

#compile and extract text with specific patterns
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
print(matches)
