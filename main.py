import cv2 as cv
import easyocr
import matplotlib.pyplot as plt

img = cv.imread('test/img1.jpg')

reader = easyocr.Reader(['en'], gpu=False)

text = reader.readtext(img)

for t in text:
    print(t)
    bbox, text, score =t

    cv.rectangle(img, bbox[0], bbox[2],(0,0,255),2)
    cv.putText(img,text, bbox[0], cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2 )


plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.show()