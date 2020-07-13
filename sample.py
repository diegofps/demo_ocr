#!/usr/bin/python3

from PIL import Image
import pytesseract
import io

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
img_filepath = "dataset/saude.png"

def read_image(filepath):
    with open(filepath, "rb") as fin:
        data = bytearray(fin.read())
        data = io.BytesIO(data)
        return Image.open(data)

def read_image2(filepath):
    img = Image.open(filepath)
    return img

# Read image
img = read_image(img_filepath)
#img = read_image2(img_filepath)

# Parse text
text = pytesseract.image_to_string(img, lang="por")
#text = pytesseract.image_to_string(img, lang="eng")

print(text)

