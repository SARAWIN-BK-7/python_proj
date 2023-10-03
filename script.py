import numpy as np 
import cv2
import cvzone


cap = cv2.VideoCapture(0)
cap.set(3,200)
cap.set(4,380)


while cap.isOpened():
    
    ret, frame = cap.read()
    
    # PreProcess 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    
    blur = cv2.GaussianBlur(gray, (5,5),7) 
    
    edges = cv2.Canny(blur, 100,255)
    
    kernel = np.ones((3,3), np.uint8)
    
    dila = cv2.dilate(edges, kernel, 1)
    

    
    
    
    
    img = cvzone.stackImages([gray, frame, blur, dila],2,1)
    
    cv2.imshow('Image',img)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break 

if __name__ == '__main__': 
    cap.release() 
    cv2.destroyAllWindows()
        