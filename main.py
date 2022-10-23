import cv2
import numpy as np
import matplotlib.pylab as plt

from process import *
from calibrate import *
cap = cv2.VideoCapture('/Users/swapna/Desktop/LaneDetection/test.mov')

while cap.isOpened():
        
        ret,frame_orig= cap.read()
        frame_clone   = frame_orig.copy()
        
        if not ret:
                print("Can't receive frame (stream end?). Exiting.")
                break
        
        frame, contours = process(frame_clone)
        
        #region calibration
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == 1:

                cv2.imshow('original frame', frame_clone)
                cv2.setMouseCallback('original frame', click_event, frame_clone)
                cv2.waitKey(0)
                print("******", coords_calib)
                
                threshold = calculate_threshold(coords_calib, frame_clone)
                
                
        #endregion calibration
           
        #frame_channels3 = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
        #frame_display   = np.concatenate((orig_frame, frame_channels3), axis=1)  
        #for contour in contours:
        #        print(cv2.contourArea(contour=contour))
        
        cv2.drawContours(frame_clone,contours,-1,(0,255,0),10)
        cv2.imshow('original frame', frame_clone)
        
        if cv2.waitKey(1) == ord('q'):
                break
        
cap.release()
cv2.destroyAllWindows()