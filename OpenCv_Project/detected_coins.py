import cvzone  
import cv2 as cv 
import numpy as np
 

vid = cv.VideoCapture(0) 
vid.set(3, 640)
vid.set(4, 480)

camera = True 


def empty():
    pass 

cv.namedWindow("Settings")
cv.resizeWindow("Settings", 640, 240)
cv.createTrackbar("Threshold1", "Settings", 50, 255, empty)
cv.createTrackbar("Threshold2", "Settings", 100, 255, empty)


def PreProcess1(image):
    
    # imgGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(image, (5, 5), 3) # (15, 15),0
    threshold1 = cv.getTrackbarPos("Threshold1", "Settings")
    threshold2 = cv.getTrackbarPos("Threshold2", "Settings")
    
    # Canny Edge Detection 
    imgEdge = cv.Canny(imgBlur, threshold1, threshold2)
    
    # Kernel Matrix 
    kernel = np.ones((3,3), np.uint8)
    dila = cv.dilate(imgEdge, kernel, iterations=1)    
    
    # Morphology 
    imgMorph = cv.morphologyEx(dila, cv.MORPH_CLOSE, kernel) 
    
    imgPre = imgMorph.copy()
    
    return imgPre


def PreProcess2(image): 
    
    imgGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) 
    imgBlur = cv.GaussianBlur(imgGray, (15, 15), 0)
    thresh = cv.adaptiveThreshold(imgBlur, 255, 
                                  cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv.THRESH_BINARY_INV, 11,1)
     
    kernel = np.ones((1,1), np.uint8)
    closing = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=5)
    
    result = closing.copy() 
    

    return result
    

while vid.isOpened():
    
    ret, img = vid.read()
    imgPre = PreProcess2(img) 
    
    conts, hierachy = cv.findContours(imgPre cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cnt in conts:
        area = cv.contoursArea(cnt)
        
        if area < 2000 or area > 3500:
            ellipse = cv.fitEllipse(cnt)    
        
    
    
    
    
    cv.imshow("Image", imgPre)
    

    if cv.waitKey(5) & 0xFF == ord('q'):
        break 


if __name__ == '__main__': 
    cv.release() 
    cv.destroyAllWindows()
    