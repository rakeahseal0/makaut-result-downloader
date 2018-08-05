import cv2
from PIL import Image
from pytesseract import image_to_string
import os
import sys
import time

sem=6


filePath=sys.path[0]+"/sem"+str(sem)+"/"

w=486
h=548
fortune=0
x=os.listdir(filePath)

def extract_num():
	global fortune
	null=0

	for i in range(1,len(x)):
		print("----"+str(i))
		imag=cv2.imread(filePath+x[i])
		crop_imag=imag[h:h+50,w:w+80]
		img = cv2.resize(crop_imag, (300,300))
		grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		retval, threshold2 = cv2.threshold(grayscaled,255,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		#cv2.imshow("test",threshold2)
		#cv2.waitKey(2000)
		cv2.imwrite('test.png',threshold2)

		im=Image.open(sys.path[0]+"/test.png")
		num=image_to_string(im)
		if(num>"8.62"):
			print("\t\t\t\ttopper----->"+num+"\t"+x[i])
			fortune+=1
		elif(num<"2"):
			null+=1
		else:
			print("\t\tless----->"+num)
	print(str(fortune)+"-"+str(null))
	




if __name__ == '__main__':
	extract_num()




