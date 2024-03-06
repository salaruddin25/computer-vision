import cv2
import numpy as np

# Path to the input image
image_path = '/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp'

# Read the input image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define the kernel for dilation
kernel = np.ones((5, 5), np.uint8)

# Apply the dilation operation
dilation_result = cv2.dilate(image, kernel, iterations=1)

# Display the original and dilated images
cv2.imshow('Original Image', image)
cv2.imshow('Dilation Result', dilation_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
