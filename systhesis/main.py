import numpy as np 
import cv2
import os 
from matplotlib import pyplot as plt 
import random  

bg_folder = ""
obj_folder = ""


obj_classes = ['']


train_path = ""
test_path = "" 
valid_path = "" 


def countFileInfoder(path):
    
    resualt = len([name for name in os.listdir(path)
                   if os.path.isfile(os.path.join(path, name))
                   ])
    return resualt 

n_items = countFileInfoder(bg_folder)
print(n_items)


def save_dataset(img_folder, img_data, class_index, kpts): 
    n_items = countFileInfoder(img_folder) # How many files in folder 
    img_filename = os.path.join(img_folder, "bordeaux_exp_qr_{:05d}.jpg".format(n_items)) 
    label_filename = img_filename.replace("images", "lables").replace("jpg", "txt") 
    
    
    keypoints_label = kpts.T.flatten() 
    # keypoints_label=np.array([origin_x,origin_y,width,height])
    # keypoints_label=np.array([origin_x+width/2,origin_y+height/2,width,height])
    
    keypoints_text=np.array2string(keypoints_label, formatter={'float_kind':lambda x: "%.4f" % x})
    # print(keypoints_text)
    img_data=cv2.cvtColor(img_data,cv2.COLOR_BGR2RGB)
    
    cv2.imwrite(img_filename,img_data)
    with open(label_filename, 'w') as f:
        f.write("{0} ".format(class_index))
        f.write(keypoints_text[1:-1])
    
