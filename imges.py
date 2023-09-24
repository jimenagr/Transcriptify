from PIL import Image
from pytesseract import *

def image(img):
    pytesseract.tesseract_cmd = r'tesseract\tesseract.exe'

    resultado = pytesseract.image_to_string(img)

    return resultado