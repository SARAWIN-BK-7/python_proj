import cv2
import imutils 

image = cv2.imread("/image/excoins_1.jpg")
print(image)
image = imutils.resize(image, width=500) 

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
blur = cv2.GaussianBlur(gray, (3,3),7)

t,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
cv2.imshow("threshold",thresh)

cnts = cv2.findContours(thresh,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
clone = image.copy()

i = 0

for c in cnts:
    # compute the area and the perimeter of the contour
    area = cv2.contourArea(c)
    
    if area > 0:

        i = i+1

        cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
        
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        
        cv2.putText(clone, "#{}".format(i), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX,
            1.25, (0, 255, 255), 4)
    else:
        pass
    
cv2.imshow("original",image)
cv2.imshow("counter",clone)
cv2.waitKey(0)