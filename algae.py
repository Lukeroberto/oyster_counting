import matplotlib.pyplot as plt
import numpy as np
import cv2

def load_image(filepath):
    """ 
    Load image as grayscale
    """
    
    return cv2.imread('tetra_ex.jpg', 0)

def undistort_vignette(original_image, calibration_image):
    """ 
    Takes PSD (calibration image) and uses to remove vignette from original image
    """
    
    return (original_image / calibration_image)

def threshold_image(undistorted_image):
    """
    Takes an image and performs OTSU thresholding 

    returns a binary image
    """
    ret3,mask = cv2.threshold(corrected_image.astype('uint8'),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return mask

def count_components(corrected):
    """
    counts connected components on a thresholded image
    """
    # threshold
    th, threshed = threshold_image(corrected)

    # findcontours
    cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]


    # filter by area
    s1= 3
    s2 = 20
    xcnts = []
    for cnt in cnts:
        if s1<cv2.contourArea(cnt) <s2:
            xcnts.append(cnt)

    return cnts, len(xcnts)

