import os
import numpy as np
import pandas as pd
import shutil
import cv2
from glob import glob
import json
from tqdm import tqdm
from PIL import Image

scene = '7'
# Note: The color values here are in RGB format
RGB = {
    'LGeA&V': (0, 255, 127),
    'GcVs': (0, 255, 50),
    'RGeA': (220, 20, 60),
    'RGeV': (0, 191, 255),
    'GDA': (255, 20, 20),
    'RGA': (220, 20, 100),
    'RGV': (0, 50, 255),
    'PHA': (255, 20, 147),
    'PV': (0, 0, 225),
    'IVC': (127, 0, 255),
    'LGA': (200, 50, 50),
    'LGV': (50, 50, 200),
    'CHA': (255, 0, 147),
    'SA': (255, 105, 180),
    'LcVs': (200, 255, 0)
}

def open_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

data = open_json('S7.json')
shapes = data['shapes']

# Read the original image to get its dimensions
img = cv2.imread('S7.png')
height, width, _ = img.shape  # Get the dimensions of the original image

# Initialize a 3-channel image with the same size as the original image
img_data = np.zeros((height, width, 3), dtype=np.uint8)

for shape in shapes:
    label = shape['label']
    if label in RGB:  # Check if the label is in the RGB dictionary
        # Convert the coordinates from JSON to pixel coordinates
        location = np.asarray(shape["points"], dtype=np.int32)
        # Convert RGB to BGR
        bgr_color = (RGB[label][2], RGB[label][1], RGB[label][0])
        cv2.fillPoly(img_data, [location], color=bgr_color)

# Save the mask as a color image
cv2.imwrite('S7_mask.png', img_data)

# Overlay the mask on top of S7.png with opacity set to 0.7
mask = cv2.imread('S7_mask.png')  # Read the mask image

# Check if the image size and the number of channels are consistent
if img.shape != mask.shape:
    print("Adjusting the mask size to match the original image")
    mask = cv2.resize(mask, (img.shape[1], img.shape[0]))  # Adjust the mask size

# Extract the non-black parts from the mask
mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
_, mask_binary = cv2.threshold(mask_gray, 1, 255, cv2.THRESH_BINARY)  # Binarize, non-black parts are 255

# Convert the binary mask to 3 channels
mask_binary_rgb = cv2.cvtColor(mask_binary, cv2.COLOR_GRAY2BGR)

# Create a transparent mask
alpha = 0.5  # Opacity
masked = img.copy()
masked[mask_binary_rgb > 0] = cv2.addWeighted(img, 1 - alpha, mask, alpha, 0)[mask_binary_rgb > 0]

# Save the result
cv2.imwrite('S7_masked.png', masked)
