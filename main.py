import cv2 as cv
import easyocr
import matplotlib.pyplot as plt

img = cv.imread('test/img2.jpg')

reader = easyocr.Reader(['en'], gpu=False)

