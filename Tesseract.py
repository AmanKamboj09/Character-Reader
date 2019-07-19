from PIL import Image
import pytesseract

im = Image.open("sample1.jpg")

text = pytesseract.image_to_string(im, config = '')

print(text)
