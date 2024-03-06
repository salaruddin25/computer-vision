import cv2

source_image_path = '/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp'
source_image = cv2.imread(source_image_path)

x, y, width, height = 500, 500, 900, 900
roi = source_image[y:y+height, x:x+width].copy()
source_image[y:y+height, x:x+width] = roi

cv2.imshow('Original Image', source_image)
cv2.imshow('Cropped ROI', roi)
cv2.imshow('Pasted ROI', source_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
