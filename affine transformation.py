import cv2
import numpy as np

image_path = "/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp"
original_image = cv2.imread(image_path)

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

matrix = cv2.getAffineTransform(pts1, pts2)
result_image = cv2.warpAffine(original_image, matrix, (original_image.shape[1], original_image.shape[0]))

cv2.imshow("Original Image", original_image)
cv2.imshow("Affine Transformed Image", result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
