import cv2
import matplotlib.pyplot as plt
import numpy as np

def dilate_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if img is None:
        print("Error: Unable to read the image.")
        return

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3, 3), np.uint8)
    dilated_img = cv2.dilate(gray_img, kernel, iterations=1)

    plt.figure(figsize=(10, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(dilated_img, cmap='gray')
    plt.title('Dilated Image')

    plt.show()

# Example usage
image_path = '/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp'
dilate_image(image_path)
