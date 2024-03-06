import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = '/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Unable to load the image.")
    exit()

edges = cv2.Canny(img, 50, 150)

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Edge Detection (Canny)')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.show()
