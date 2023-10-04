import cv2
import numpy as np  


W = 400 

def my_ellipse(img, angle):
    thickness = 2
    line_type = 8 
    
    cv2.ellipse(img,
                (W // 2, W//2),
                (W // 4, W//16), 
                angle,
                0,
                360,
                (255,0,0), 
                thickness,
                line_type)

def my_filled_circle(img, center):
    thickness = -1
    line_type = 8
    cv2.circle(img,
               center,
               W // 32,
               (0, 0, 255),
               thickness,
               line_type)

    
def my_polygon(img): 
    line_type = 8
    
    # Create some points
    ppt = np.array([[W / 4, 7 * W / 8], [3 * W / 4, 7 * W / 8],
                    [3 * W / 4, 13 * W / 16], [11 * W / 16, 13 * W / 16],
                    [19 * W / 32, 3 * W / 8], [3 * W / 4, 3 * W / 8],
                    [3 * W / 4, W / 8], [26 * W / 40, W / 8],
                    [26 * W / 40, W / 4], [22 * W / 40, W / 4],
                    [22 * W / 40, W / 8], [18 * W / 40, W / 8],
                    [18 * W / 40, W / 4], [14 * W / 40, W / 4],
                    [14 * W / 40, W / 8], [W / 4, W / 8],
                    [W / 4, 3 * W / 8], [13 * W / 32, 3 * W / 8],
                    [5 * W / 16, 13 * W / 16], [W / 4, 13 * W / 16]], np.int32)
    
    
    ppt = ppt.reshape((-1, 1, 2))
    
    cv2.fillPoly(img, [ppt], (255, 255, 255), line_type)
    
    
def my_line(img, start, end):
    
    thickness = 2
    line_type = 8 
    
    cv2.line(img, 
             start, 
             end, 
             (0, 0, 0), 
             thickness,
             line_type)


atom_window = "Drawing 1 : Atom" 
rook_window = "Drawing 2 : Rook" 


# Create black empty images 
size = W, W, 3 

atom_image = np.zeros(size, dtype=np.uint8) 
rook_image = np.zeros(size, dtype=np.uint8)


# 1. a. Create ellipses 
my_ellipse(atom_image, 90)
my_ellipse(atom_image, 0)
my_ellipse(atom_image, 45)
my_ellipse(atom_image, -45)


# 1 b. Creating Circles 
my_filled_circle(atom_image, (W//2,W//2))

# 2. Drawing a Rook 

# --------------------------------
# 2. a. Creating a convex polygon
my_polygon(rook_image)

cv2.rectangle(rook_image,
              (0,7*W//8),
              (W,W),
              (0, 255, 255),
              -1,
              8)

#  2.c. Create a few lines
my_line(rook_image, (0, 15 * W // 16), (W, 15 * W // 16))
my_line(rook_image, (W // 4, 7 * W // 8), (W // 4, W))
my_line(rook_image, (W // 2, 7 * W // 8), (W // 2, W))
my_line(rook_image, (3 * W // 4, 7 * W // 8), (3 * W // 4, W))
cv2.imshow(atom_window, atom_image)
cv2.moveWindow(atom_window, 0, 200)
cv2.imshow(rook_window, rook_image)
cv2.moveWindow(rook_window, W, 200)
cv2.waitKey(0)
cv2.destroyAllWindows()