import cv2
import cvzone
import numpy as np 
from cvzone.ColorModule import ColorFinder 

cap = cv2.VideoCapture(0)
cap.set(3,200)
cap.set(4,480)
cam = True 

totalMoney = 0

myColorFinder = ColorFinder(False)

# Custom Orange Color 
hsvVals = {
            'hmin': 10,
            'smin': 55,
            'vmin': 215,
            'hmax': 42,
            'smax': 255,
            'vmax': 255
        }

def empty(): 
    pass  

cv2.namedWindow("Settings")
cv2.resizeWindow("Settings", 640, 240)
cv2.createTrackbar("Threshold1", "Settings", 50,255, empty)
cv2.createTrackbar("Threshold2", "Settings", 100,255, empty)

def PreProcess(img): 
    
    imgPre = cv2.GaussianBlur(img,(5,5),3)
    threshold1 = cv2.getTrackbarPos("Threshold1", "Settings")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Settings")
    imgPre = cv2.Canny(imgPre, threshold1, threshold2)
    kernel = np.ones((3,3), np.uint8) 
    imgPre = cv2.dilate(imgPre, kernel,iterations=1)
    imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)
    
    return imgPre


while cam:
    
    ret, img = cap.read() 
    imgPre = PreProcess(img)
    imgContours, conFound = cvzone.findContours(img, imgPre,minArea=20)
    totalMoney = 0
    
    if conFound: 
        for contour in conFound:
            peri = cv2.arcLength(contour['cnt'], True) 
            approx = cv2.approxPolyDP(contour['cnt'], 0.02 * peri, True)
            
            if len(approx)>5:
                # print(contour['area'])   
                area = contour['area']
                
                # imgColor, _ = myColorFinder.update(img, hsvVals)
                
                if area<2050:
                    totalMoney += 5
                elif 2050 <area<2500:
                    totalMoney +=1
                else:
                    totalMoney +=2 
                    
    print(totalMoney)        
    
    imgStacked = cvzone.stackImages([img, imgPre, imgContours],2,1) 
    cvzone.putTextRect(imgStacked,f'Rs.{totalMoney}', (50, 50) )   
    # cv2.imshow("Image", img) 
    # cv2.imshow("ImagePre", imgPre) 
    
    
    cv2.imshow("Image", imgStacked) 
    # cv2.imshow("ImageColor", imgColor)
    
    if cv2.waitKey(5) & 0xFF == ord('q') :
        break 

if __name__ == '__main__': 
    cv2.release() 
    cv2.destroyAllWindows() 
    
