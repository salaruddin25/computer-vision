import cv2

image_path = "/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp"
original_image = cv2.imread(image_path)

height, width = original_image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), -270, 1)
rotated_image = cv2.warpAffine(original_image, rotation_matrix, (width, height))

cv2.imshow("Rotated 270 degrees", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
