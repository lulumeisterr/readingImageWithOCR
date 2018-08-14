from PIL import Image
import pytesseract as ocr
import json,requests , csv
import cv2
import numpy

phrase = ocr.image_to_string(Image.open('/home/lucasn/Desktop/exame.jpg'))
print(phrase)







