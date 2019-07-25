import matplotlib.pyplot as plt
import numpy as np
import cv2

def load_image(filepath):
    """ Load image as grayscale"""
    
    return cv2.imread('tetra_ex.jpg', 0)

def undistort_vignette(original_image, calibration_image):
    """ Takes PSD (calibration image) and uses to remove vignette from original image"""
    
    return (original_image / calibration_image)

def plot_calibration(original_image, calibration_image):
    original_image = load_image(original_image)
    calibration_image = load_image(calibration_image)
    
    corrected = undistort_vignette(original_image, calibration_image)
    
    ims = [original_image, calibration_image, corrected]
    
    fig = plt.figure(figsize=(8,11))
    for i in range(3):
        ax = fig.add_subplot(1, 3, i + 1)
        ax.imshow(ims[i], cmap='gray')
        ax.axis('off')
    plt.savefig("temp/image_calibration.jpg")
    plt.show()
    
def plot_thresholded_image(corrected_image):
    ret3,mask = cv2.threshold(corrected_image.astype('uint8'),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    plt.imshow(mask, cmap="gray")
    plt.title("Thresholded")
    plt.savefig("temp/thresholded_image.jpg")
    plt.show()
    
def count_dots(corrected_image):
    ## threshold
    th, threshed = cv2.threshold(255 - corrected.astype('uint8'), 100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

    ## findcontours
    cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]


    ## filter by area
    s1= 1
    s2 = 20
    xcnts = []
    for cnt in cnts:
        if s1<cv2.contourArea(cnt) <s2:
            xcnts.append(cnt)

    print(f"Number of dots: {len(xcnts)}")
    return len(xcnts)

def plot_histogram(image, name):
    plt.hist(corrected.ravel(), bins=256)
    plt.savefig("tempt/{}_histogram.jpg".format(name))
    plt.show()