#requires webcam, might write code for ipcam idk yet that involves work

import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
print("Try To focus item inside the Rectangle. Press the 'b' key to close")
time.sleep(2)
while True:
  
    _, frame = cap.read()

    # Converts BGR to HSV color codes
    #It uses BGR not RGB, weird isn't it?
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame = cv2.rectangle(frame,(500,400), (100,100), (0,0,0), 2)


#Primary colors
    # range of blue done
    lower_blue = np.array([102,100,100],np.uint8)
    upper_blue = np.array([122,255,255],np.uint8)

    #range of red done
    lower_red = np.array([169,100,100],np.uint8)
    upper_red = np.array([189,255,255],np.uint8)

    #range of yellow done
    lower_yellow = np.array([20,100,100],np.uint8)
    upper_yellow = np.array([40,255,255],np.uint8)

#Secondary Colors
#idk if these will interfere with the primary colors because they overlap
    #range of green done
    lower_green = np.array([50,100,100],np.uint8)
    upper_green = np.array([70,255,255],np.uint8)

    #range of orange done
    lower_orange = np.array([9,100,100],np.uint8)
    upper_orange = np.array([29,255,255],np.uint8)

    #range of purple done
    lower_purple = np.array([125,100,100],np.uint8)
    upper_purple = np.array([145,255,255],np.uint8)

    # defining colors and stuff
    blue=cv2.inRange(hsv,lower_blue,upper_blue)
    red=cv2.inRange(hsv,lower_red,upper_red)
    yellow=cv2.inRange(hsv,lower_yellow,upper_yellow)
    green=cv2.inRange(hsv,lower_green,upper_green)
    orange=cv2.inRange(hsv,lower_orange,upper_orange)
    purple=cv2.inRange(hsv,lower_purple,upper_purple)


#boring stuff for the computer to deal with
    this = np.ones((5 ,5), "uint8")

    red=cv2.dilate(red, this)
    bdb=cv2.bitwise_and(frame, frame, mask = red)

    blue=cv2.dilate(blue,this)
    bdb1=cv2.bitwise_and(frame, frame, mask = blue)

    yellow=cv2.dilate(yellow,this)
    bdb2=cv2.bitwise_and(frame, frame, mask = yellow)

    orange=cv2.dilate(orange,this)
    bdb3=cv2.bitwise_and(frame, frame, mask = orange)

    green=cv2.dilate(green,this)
    bdb4=cv2.bitwise_and(frame, frame, mask = green)

    purple=cv2.dilate(purple,this)
    bdb5=cv2.bitwise_and(frame, frame, mask = purple)

#this tracks the color and draws boxes around the objects

#Tracks Red
    (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>400):

			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
			cv2.putText(frame,"Red",(x,y),cv2.FONT_HERSHEY_TRIPLEX, 3, (0,0,255))

	#Tracks Blue
    (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>400):
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
			cv2.putText(frame,"Blue",(x,y),cv2.FONT_HERSHEY_TRIPLEX, 3, (255,0,0))

#Tracks Yellow
    (_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>400):
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)
			cv2.putText(frame,"Yellow",(x,y),cv2.FONT_HERSHEY_TRIPLEX, 3, (0,255,255))
#Tracks Orange
    (_,contours,hierarchy)=cv2.findContours(orange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>400):
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,165,255),3)
			cv2.putText(frame,"Orange",(x,y),cv2.FONT_HERSHEY_TRIPLEX, 5, (0,165,255))
#Tracks Purple
    (_,contours,hierarchy)=cv2.findContours(purple,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>400):
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(128,0,128),3)
			cv2.putText(frame,"Purple",(x,y),cv2.FONT_HERSHEY_TRIPLEX, 3, (128,0,128))
#Tracks green
    (_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>400):
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,128,0),3)
			cv2.putText(frame,"Green",(x,y),cv2.FONT_HERSHEY_TRIPLEX, 3, (0,128,0))



    cv2.imshow("Color Blind Assistant",frame)
#end it by pressing b
    if cv2.waitKey(10) & 0xFF == ord('b'):
    	cap.release()
    	cv2.destroyAllWindows()
    	break
