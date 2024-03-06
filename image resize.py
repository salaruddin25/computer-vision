import cv2
import matplotlib.pyplot as plt

image_path = '/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp'
img = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img is None:
    print("Error: Unable to read the image.")
else:
    # Resize to a bigger size for display
    bigger_size = cv2.resize(img, (img.shape[1] * 15, img.shape[0] * 15))

    # Resize to a smaller size for display
    smaller_size = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

    # Display the original, bigger, and smaller images
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(bigger_size, cv2.COLOR_BGR2RGB))
    plt.title('Bigger Size')
    plt.xticks([]), plt.yticks([])  # Hide axes ticks

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(smaller_size, cv2.COLOR_BGR2RGB))
    plt.title('Smaller Size')
    plt.xticks([]), plt.yticks([])  # Hide axes ticks

    plt.show()
