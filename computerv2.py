import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = '/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp'
img = cv2.imread(image_path)

if img is None:
    print("Error: Unable to load the image.")
    exit()

# Convert the image to RGB (OpenCV uses BGR by default)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Gaussian Blur
ksize = (25, 25)
sigmaX = 0
blurred_image = cv2.GaussianBlur(img_rgb, ksize, sigmaX)

# Display the original and blurred images
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Blurred Image')
plt.imshow(blurred_image)
plt.axis('off')

plt.show()
