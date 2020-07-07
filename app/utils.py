import os
import cv2
import numpy as np


def modify_filename(org_name, text):
    if text:
        return org_name.split(".")[0] + '_' + str(text) + '.' + org_name.split(".")[1]
    else:
        return org_name
    

def transform_img(path, filename, mode):    
    ext = ['gray', 've', 'he']
    
    # Check if file already exists
    if not os.path.isfile(os.path.join(path, modify_filename(filename, ext[mode]))):
        
        # Read image in gray scale
        image = cv2.imread(os.path.join(path, filename), 0)
        
        if mode != 0:
            if mode == 1:
                # sobel_x for vertical edges
                filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
            elif mode == 2:
                # sobel_y for horizontal edges
                filter = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
            
            image = cv2.filter2D(image, -1, filter)
            
        cv2.imwrite(os.path.join(path, modify_filename(filename, ext[mode])), image)
        
    return ext[mode]


def get_num_words(sent):
	return len(sent.split(" "))