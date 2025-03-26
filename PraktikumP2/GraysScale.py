import cv2
from matplotlib import pyplot as plt

image = cv2.imread('kucing.jpg') 
# Konversi gambar ke grayscale

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Menampilkan gambar dalam grayscale
plt.imshow(image_gray, cmap='gray')
plt.title('Gambar Grayscale')
plt.axis('off')
plt.show()
