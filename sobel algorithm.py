import cv2
import numpy as np

image_path = '/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
magnitude = np.uint8(255 * magnitude / np.max(magnitude))

cv2.imshow('Original Image', img)
cv2.imshow('Sobel Filtered Image', magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
