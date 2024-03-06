import cv2

image_path = "/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp"

original_image = cv2.imread(image_path)

if original_image is not None:
    height, width = original_image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), -90, 1)
    rotated_image = cv2.warpAffine(original_image, rotation_matrix, (width, height))
    cv2.imshow("Rotated Image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to load the image.")
