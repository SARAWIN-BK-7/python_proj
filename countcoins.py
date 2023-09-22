import cv2
import numpy as np 



cap = cv2.VideoCapture(0)
cam = True 

while cam: 
    
    ret, image = cap.read()
    # print("ret: ", ret)
    # print("image: ", image)
    
    # Convert image to Gray 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    # Canny Edge Detection By OpenCv
    edge = cv2.Canny(gray, 0,255)
    # print(edge)
    
    
    cv2.imshow("Image Ori",image)
    cv2.imshow("Edge Detection", edge)
    
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break 
        
          
if __name__ == '__main__': 
    cv2.destroyAllWindows()
    
