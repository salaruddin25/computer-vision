import cv2

original_image_path = '/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp'
watermark_path = '/Users/syedsalaruddin/Downloads/img.png'  

original_image = cv2.imread(original_image_path)
watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)

alpha = 0.7
beta = 1 - alpha

watermark_resized = cv2.resize(watermark, (original_image.shape[1], original_image.shape[0]))

result = cv2.addWeighted(original_image, 1, watermark_resized, alpha, beta)

cv2.imshow('Watermarked Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
