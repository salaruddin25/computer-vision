import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Unable to read the image.")
        return

    channels = cv2.split(img)
    colors = ('b', 'g', 'r')

    plt.figure(figsize=(10, 6))

    for i, color in enumerate(colors):
        plt.plot(cv2.calcHist([channels[i]], [0], None, [256], [0, 256]), color=color)
        plt.xlim([0, 256])

    plt.title('Histogram Analysis')
    plt.xlabel('Color Level')
    plt.ylabel('Frequency')
    plt.legend(['Blue', 'Green', 'Red'])
    plt.show()

# Example usage
image_path = '/Users/syedsalaruddin/Downloads/1998-Toyota-Supra-Desktop-Wallpaper-4k.webp'
analyze_histogram(image_path)
