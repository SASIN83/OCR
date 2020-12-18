#Import Libraries
import cv2
import numpy as np
import requests
import configure
import io
import json

#Taking Input for image
try:
    x=input("Enter image location and name: ")
except:
    print("Enter valid image name: Example- x.png")

#Reading Image
img=cv2.imread(x)
#print(img)
#print(img.shape)

#Comressing and Encoding to bytes
y=x.split(".")[1]
_,compress= cv2.imencode(f'.{y}',img,[1,90])
file_bytes= io.BytesIO(compress)


#URL API OCR
url="https://api.ocr.space/parse/image"
print("Contacting Server....")
try:

    result = requests.post(url,files= {"5.png": file_bytes}, data= {"apikey":configure.API})
    #result =requests.post(url,files= {"Pictures/5.png": file_bytes}, data= {"apikey":configure.API,"isoverlayrequired": True})
    result=json.loads(result.content.decode())
    print("Connection Established.....\nCreating text file of OCR")
    
    #Creating OCR file
    with open(f"{x}OCR.txt",'a') as f:
        f.write(result["ParsedResults"][0]["ParsedText"])
        print("Text file is created")
except requests.exceptions.ConnectionError:
    print("No internet")

except Exception as e:
    print(e)
