# pip install opencv-python
# pip install pillow

import cv2
from PIL import Image
import PIL
import numpy as np
import os

# Kathakali
# Mohiniyattam
# Kuchipudi
# Bharatanatyam

filename = f'Dataset_Test_without_Background/Bharatanatyam/Bharatanatyam-1.png'
print(filename)
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
image_display = cv2.resize(image, (510, 510))

# Apply Canny edge detection
canny_edges = cv2.Canny(image, threshold1 = 50, threshold2 = 100)
image = cv2.resize(canny_edges, (510, 510))

# For Saving the image
image_tosave = Image.fromarray(image.astype(np.uint8))
image_tosave.save(f'50_100_Test/Bharatanatyam/Bharatanatyam-1.png', 'PNG')