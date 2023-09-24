import cv2
import cvzone


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cam = True 

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
    
    
    return imgPre

while cam:
    
    ret, img = cap.read() 
    
    imgPre = PreProcess(img)
    
    imgStacked = cvzone.stackImages([img, imgPre],2,1)
    # cv2.imshow("Image", img) 
    # cv2.imshow("ImagePre", imgPre) 
    cv2.imshow("Image", imgStacked) 
    
    if cv2.waitKey(5) & 0xFF == ord('q') :
        break 

if __name__ == '__main__': 
    cv2.release() 
    cv2.destroyAllWindows() 
    