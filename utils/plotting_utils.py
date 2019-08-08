from .. import algae

import numpy as np
import maptplotlib.pyplot as plt
import cv2

def plot_calibration(original_image, calibration_image):
    """
    plots the calibration images together.
    """
    original_image = algae.load_image(original_image)
    calibration_image = algae.load_image(calibration_image)
    
    corrected = algae.undistort_vignette(original_image, calibration_image)
    
    ims = [original_image, calibration_image, corrected]
    
    fig = plt.figure(figsize=(8,11))
    for i in range(3):
        ax = fig.add_subplot(1, 3, i + 1)
        ax.imshow(ims[i], cmap='gray')
        ax.axis('off')
    plt.savefig("temp/image_calibration.jpg")
    plt.show()
    
    return ims
    
def plot_thresholded_image(corrected_image):
    """
    plots the thresholded 
    """
    mask = algae.threshold_image(corrected_image)
    plt.imshow(mask, cmap="gray")
    plt.title("Thresholded")
    plt.savefig("temp/thresholded_image.jpg")
    plt.show()

def plot_histogram(image, name):
    """
    plots a histogram of pixel values
    """
    plt.hist(image.ravel(), bins=256)
    plt.title(image)
    plt.savefig("temp/{}_histogram.jpg".format(name))
    plt.show()
