import cv2
import matplotlib.pyplot as plt


image_color = cv2.imread('kucing.jpg')  
image_color = cv2.resize(image_color, (300, 300))

# Konversi ke grayscale
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

# Membuat histogram gambar berwarna
colors = ('b', 'g', 'r')
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
for i, color in enumerate(colors):
    histogram = cv2.calcHist([image_color], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color)
plt.title('Histogram Gambar Berwarna')
plt.xlabel('Intensitas')
plt.ylabel('Jumlah Piksel')

# Membuat histogram gambar grayscale
plt.subplot(1, 2, 2)
histogram_gray = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
plt.plot(histogram_gray, color='black')
plt.title('Histogram Gambar Grayscale')
plt.xlabel('Intensitas')
plt.ylabel('Jumlah Piksel')

plt.tight_layout()
plt.show()