import cv2
import numpy as np

image_path = '/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)

opening_result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
top_hat_result = cv2.subtract(image, opening_result)

cv2.imshow('Original Image', image)
cv2.imshow('Top Hat Result', top_hat_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
