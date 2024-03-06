import cv2
import numpy as np

image_path = "/Users/syedsalaruddin/Downloads/dsc5621_3nd.webp"
original_image = cv2.imread(image_path)

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply Harris Corner Detection
harris_corners = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)

# Threshold for selecting strong corners
threshold = 0.01 * harris_corners.max()

# Mark detected corners on the original image
original_image[harris_corners > threshold] = [0, 0, 255]  # Set corners to red color

# Display the original and processed images
cv2.imshow("Original Image", original_image)
cv2.imshow("Harris Corner Detection", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
