import pytesseract
from pytesseract import Output
import cv2
import json 
from os import listdir

font = cv2.FONT_HERSHEY_SIMPLEX 
org = (50, 50) 
fontScale = 0.5
color = (255, 0, 0) 
thickness = 1

path='images/'
files=listdir(path)

for file in files:
    img = cv2.imread(path+file)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    # font 
    d1={}
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        txt=d['text'][i]
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.putText(img, txt, (x,y), font, fontScale, color, thickness, cv2.LINE_AA) 
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        d1[txt]=[x,y,x+h,y+h]
        print(x,y,x+h,y+h)
        # Serializing json  
        json_object = json.dumps(d1, indent = 4) 
  
# Writing to sample.json 
        with open("sample.json", "w") as outfile: 
            outfile.write(json_object) 

    cv2.imshow('img', img)
    cv2.waitKey(1)
    cv2.imwrite(file,img)
