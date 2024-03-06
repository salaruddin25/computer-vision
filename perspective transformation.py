import cv2
import numpy as np

image_path = "/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp"
original_image = cv2.imread(image_path)

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result_image = cv2.warpPerspective(original_image, matrix, (300, 300))

cv2.imshow("Original Image", original_image)
cv2.imshow("Perspective Transformed Image", result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
