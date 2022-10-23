import cv2
import numpy as np

coords_calib = []
no_pts_calib = 5

def click_event(event, x, y, flags, image):
        if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(image, radius=3, center=(x,y),color=(0,0,255),thickness=3)
                cv2.putText(image, str(x) + ',' + str(y), (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)
                cv2.imshow('original frame',image)
                coords_calib.append((x, y))
                
                if len(coords_calib) == no_pts_calib:
                        print("Press any key to proceed to next steps.")
                

def calculate_threshold(coords, image):
        
        gray_image  = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        pixel_vals_calib = []
        
        for coord in coords_calib:
                pixel_vals_calib.append(gray_image[coord[1], coord[0]])
        
        thresh_lower =0 
        thresh_upper = 255
        
        if np.min(pixel_vals_calib)-10 > thresh_lower: 
                thresh_lower = np.min(pixel_vals_calib)-10
        if np.max(pixel_vals_calib)+10 < thresh_upper:
                thresh_upper = np.max(pixel_vals_calib)+10
        
        #binary_image = np.zeros(gray_image.shape[:2],dtype=np.uint8)
        
        #binary_image = np.where((gray_image > thresh_lower) & (gray_image < thresh_upper), 255, binary_image)
        
        return (thresh_lower, thresh_upper)