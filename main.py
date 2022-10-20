import cv2
import numpy as np
import matplotlib.pylab as plt

from process import *

cap = cv2.VideoCapture('/Users/swapna/Desktop/LaneDetection/test.mov')

while cap.isOpened():
        
        ret, orig_frame = cap.read()
        
        # if frame is read correctly ret is True
        if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
        
        frame = process(orig_frame)
        
       
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        frame_channels3 = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
        frame_display   = np.concatenate((orig_frame, frame_channels3), axis=1)  
    
        cv2.imshow('original frame', frame_display)
   
        
        if cv2.waitKey(1) == ord('q'):
                break
        
cap.release()
cv2.destroyAllWindows()