import cv2
from matplotlib import pyplot as plt

# Membaca gambar
gambar = cv2.imread('kucing.jpg')  

# Resize gambar menjadi 300x300
resized_image = cv2.resize(gambar, (300, 300))

# Crop bagian tengah gambar (100x100)
height, width = gambar.shape[:2]
start_row, start_col = height // 4, width // 4
end_row, end_col = start_row + 100, start_col + 100
cropped_image = gambar[start_row:end_row, start_col:end_col]

# Konversi ke grayscale untuk histogram
gray_image = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

# Menampilkan gambar yang di-resize dan di-crop
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.title('Resized 300x300')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.title('Cropped 100x100')
plt.axis('off')

# Menampilkan histogram grayscale
plt.subplot(1, 3, 3)
plt.hist(gray_image.ravel(), bins=256, color='gray', alpha=0.7)
plt.title('Histogram Grayscale')

plt.tight_layout()
plt.show()
