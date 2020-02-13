# Full algae counting flow 
# Uses toupcam api to take a snapshot of the current camera view. Then calibrates and counts using the cv2 library.

import numpy as np
import cv2

import matplotlib.pyplot as plt
import algae
import utils.plotting_utils as aplt

from os import listdir


images = []
calib = algae.load_image("test_images/" + image_locs[1])

for i, loc in enumerate(image_locs):
    images.append(algae.load_image("test_images/" + loc))
    if images[i].shape == calib.shape:
        images[i] = algae.undistort_vignette(images[i], calib)
    images[i] = algae.threshold_image(images[i])


def f(i):
    plt.imshow(images[i], cmap="gray")
    plt.show()
    print("Image: ", image_locs[i])
    print("Counted Dots: ", algae.count_components(images[i])[1])
    
# interact(f, i=(0, len(image_locs) - 1))



# Next steps:
#
# 1. Look at toupcam api, understand toupcam.Toupcam.Open(...)
# 2. Understand callback structure
# 3. Maybe self.hcam.PullImageV2(self.buf, 24, None) will work?
# 4. Use input() to signal snapshot (Tell user to manually calibrate first, then hit enter)
# 5. Save this in ../snapshots
# 6. Run algae code above on calibrated image and sample image
# 7. Output algae count
# 8. Return this info to user 