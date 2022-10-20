import numpy as np
import cv2


def get_roi(img, vertices):
        mask = np.zeros_like(img)
        #channel_count = img.shape[2]
        match_mask_color = 255
        
        cv2.fillPoly(mask, vertices, match_mask_color)
        masked_image = cv2.bitwise_and(img, mask)
        
        return masked_image


def draw_lines(img, lines):
        
        img = np.copy(img)
        blank_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
        
        for line in lines:
                for x1, y1, x2, y2 in line:
                        cv2.line(blank_img, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)
        
        img = cv2.addWeighted(img, 0.8, blank_img, 1, 0.0)
        return img

def process(image):
        
        #print(image.shape)
        
        height = image.shape[0]
        width = image.shape[1]
        
        roi_vertices = [(0, height), (width/2, height/2), (width, height)]
        
        gray_image  = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        canny_image = cv2.Canny(gray_image, 150, 200)
        
        cropped_image = get_roi(canny_image, np.array([roi_vertices], np.int32),)
        
        #lines = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi/180, threshold=50,
        #                        lines=np.array([]), minLineLength=40, maxLineGap=200)
        
        #image_lines = draw_lines(image, lines)
        return cropped_image