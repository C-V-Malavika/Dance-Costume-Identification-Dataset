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

image_files = [(file, dirs[0]) for dirs in os.walk('./Dataset_Test', topdown = False) for file in dirs[2]]

for item in image_files:

    print(item)

    folder = item[1]
    
    # Load an image in gray scale
    filename = f'{folder}/{item[0]}'
    print(filename)
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    image_display = cv2.resize(image, (510, 510))

    # Apply Canny edge detection
    canny_edges = cv2.Canny(image, threshold1 = 50, threshold2 = 150)
    image = cv2.resize(canny_edges, (510, 510))

    # For Saving the image
    image_tosave = Image.fromarray(image.astype(np.uint8))
    image_tosave.save(f'50_150_Test/{folder.strip('./Dataset_Test\\')}/{item[0]}', 'PNG')

# image_files = [(file, dirs[0]) for dirs in os.walk('./', topdown = False) for file in dirs[2] if dirs[0] != './50_150_Canny' or file != 'Canny.py']

# for item in image_files:

#     folder = item[1].strip("./")
    
#     # Load an image in gray scale
#     filename = f'{folder}/{item[0]}'
#     print(filename)
#     image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
#     image_display = cv2.resize(image, (510, 510))

#     # Apply Canny edge detection
#     canny_edges = cv2.Canny(image, threshold1 = 50, threshold2 = 150)
#     image = cv2.resize(canny_edges, (510, 510))

#     # For Saving the image
#     image_tosave = Image.fromarray(image.astype(np.uint8))
#     image_tosave.save(f'50_150_Canny/{folder}/{item[0]}', 'PNG')

# for i in range(101, 111):

#     # Load an image in gray scale
#     filename = f'Kathakali/Kathakali-{i}.png'
#     print(filename)
#     image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
#     image_display = cv2.resize(image, (510, 510))

#     # Apply Canny edge detection
#     canny_edges = cv2.Canny(image, threshold1 = 50, threshold2 = 100)
#     image = cv2.resize(canny_edges, (510, 510))

#     # For Saving the image
#     image_tosave = Image.fromarray(image.astype(np.uint8))
#     image_tosave.save(f'50_100_Canny/Kathakali/Kathakali-{i}.png', 'PNG')