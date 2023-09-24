import cv2
# import numpy as np 
import imutils 



cap = cv2.VideoCapture(0)
cam = True 

while cam: 
    
    ret, image = cap.read()
    # print("ret: ", ret)
    # print("image: ", image)
    
    # Convert image to Gray 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    
    # Gaussian Blur Gray Image
    blur = cv2.GaussianBlur(gray,(3,3),7)
    
    # Threshold 
    t, threshold = cv2.threshold(blur, 20,255,cv2.THRESH_BINARY)
    cv2.imshow("threshold", threshold)
    
    # Find Contours 
    
    cnts = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    clone = image.copy()
    
    i = 0 
    
    for c in cnts:
        # Compute the area and the perimeter of the contour 
        area = cv2.contourArea(c) 
        
        if area > 0:
            i=i+1
            
            cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
            
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            cv2.putText(clone, "*{}".format(i), (cX -20, cY), cv2.FONT_HERSHEY_SIMPLEX,
                       1.25, (255, 255, 255), 4)  
        else :
            pass 
        
    """
    
    # Canny Edge Detection By OpenCv
    # edge = cv2.Canny(gray, 0,255)
    # print(edge)
    """
    
    cv2.imshow("Image Ori",image)
    cv2.imshow("Threshold", clone)
    
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break 
        
          
if __name__ == '__main__': 
    cv2.destroyAllWindows()
    
