import matplotlib.pyplot as plt
import numpy as np
import cv2

def load_image(filepath):
    """ 
    Load image as grayscale
    """
    
    return cv2.imread(filepath, 0)

def undistort_vignette(original_image, calibration_image):
    """ 
    Takes PSD (calibration image) and uses to remove vignette from original image
    """
    
    return (original_image / calibration_image)

def threshold_image(image):
    """
    Takes an image and performs OTSU thresholding 

    returns a binary image
    """
    ret3,mask = cv2.threshold(image.astype('uint8'),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return mask

def component_area_stats(cnts):
    """
    For now returns the smallest contour area and upper quartile
    """
    
    contour_areas = np.zeros(len(cnts))
    for i, c in enumerate(cnts):
        contour_areas[i] = cv2.contourArea(c)
        
    return np.min(contour_areas), np.percentile(contour_areas, 75)

def count_components(corrected):
    """
    counts connected components on a thresholded image
    """
    # threshold
    threshed = threshold_image(corrected)

    # findcontours
    cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

    area_min, area_max = component_area_stats(cnts)

    # filter by area
    xcnts = []
    for cnt in cnts:
        if area_min <cv2.contourArea(cnt) < area_max:
            xcnts.append(cnt)

    return cnts, len(xcnts)

