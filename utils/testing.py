import numpy as np
import matplotlib.pyplot as plt

def generate_test_images(num_images, area, component_range):
    """
    Generates N 3000x3000 images with random components of certain area. Saves them to the test_images/Auto-Generated folder.
    """
    IMAGE_SIZE = 3000
    
    dx, dy = int(np.sqrt(area)), int(np.sqrt())
    for n in range(num_images):
        temp_image = np.zeros((IMAGE_SIZE, IMAGE_SIZE))
        
        # Sample a location
        n_components = np.random.randint(component_range)
        
        # Place the components somewhere in the image
        for component in range(n_components):
            x, y = np.random.randint(IMAGE_SIZE, )

            temp_image[x: x+dx, y: y+dy] = 255

        # Save the image
        plt.imsave(temp_image, "../test_images/test_{}_size_{}_components_{}.jpg".format(n, area, n_components))
        