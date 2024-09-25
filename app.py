import pytesseract
from PIL import Image

# Example OCR function
def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='eng+hin')
    return text
