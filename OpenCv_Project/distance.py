import cv2
import imutils 
import numpy as np 
import sys 
import tkinter as tk 
from tkinter import filedialog
import time 


def find_marker(img): 
    
    #Convert the image to gray, blur and Edges Detection 
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5,5), 0) 
    threshold = cv2.threshold(blurred, 200,255,cv2.THRSH_BINARY)[1]
    edges = cv2.Canny(threshold, 10,30)
    
    # Find the contours in the edged image and keep the largerst one; 
    cnts = cv2.findContours(edges.copy(),cv2.RETR_LIST,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key = cv2.contoursArea)
    
    # Compute the bounding box of the paper region and return;
    return cv2.minAreaRect(c) 

def distance_to_cam(knowWidth, focalLength, perWidth):
    # Compute and return the distance from the mark to the camera 
    return (knowWidth*focalLength)/ perWidth 


def imshow(pic): 
    cv2.imshow("Output", pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

# initialize know parameter 

KNOWN_DISTANCE = 0.75
KNOWN_WIDHT = 0.21
WriteFile = False  # Write output to Video file 

root = tk.Tk() 
root.withdraw()

file_path = filedialog.askopenfilename()

if not file_path: 
    sys.exit("Please select folder of image...") 
    
# Load test Video 

cap = cv2.VideoCapture(file_path)
time.sleep(2.0)


ret, image = cap.read() 
marker = find_marker(image) 

P = marker[1][0] # width in px 
focallength = (marker[1][0] * KNOWN_DISTANCE)/KNOWN_WIDHT

# Write Video File 

if WriteFile:
    h, w = image.shape[:2]
    fource = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter('outpy.mp4', fource, 20, (w, h))


while True: 
    ret, frame = cap.read() 
    if ret == False: break
    
    marker = find_marker(frame)
    meters = distance_to_cam(KNOWN_WIDHT, focallength, marker[1][0])
    box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker) 
    box = np.int0(box) 
    cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
    cv2.putText(frame, "%.2f m "%(meters), 
                (frame.shape[1]-300,
                 frame.shape[0]-20,
                 cv2.FONT_HERSHEY_SIMPLE,
                 2.0,
                 (0, 255, 0), 
                 3
                 ))

    cv2.imshow('image',frame) 
    if WriteFile : 
        out.write(frame) 
    time.sleep(0.1) 
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break 
        
cap.release() 
if WriteFile : 
    out.release()  
    
cv2.destroyAllWindows()
    