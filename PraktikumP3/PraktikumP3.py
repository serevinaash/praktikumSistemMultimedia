import cv2
import os
import matplotlib.pyplot as plt

# Direktori input dan output
input_dir = 'input_images/'
output_dirs = {
    'resized': 'output_images/resized/',
    'cropped': 'output_images/cropped/',
    'flipped': 'output_images/flipped/',
    'rotated': 'output_images/rotated/'
}

# Membuat folder output jika belum ada
for dir in output_dirs.values():
    try:
        os.makedirs(dir, exist_ok=True)
        print(f"Folder dibuat: {dir}")
    except Exception as e:
        print(f"Gagal membuat folder {dir}: {e}")

# Mendapatkan daftar file gambar di direktori input
images = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.jpeg', '.png'))][:10]

# Memproses setiap gambar
for image_name in images:
    image_path = os.path.join(input_dir, image_name)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Gagal membaca gambar: {image_name}")
        continue

    try:
        # Resize gambar dengan mempertahankan rasio aspek
        resized = cv2.resize(image, (400, 400), interpolation=cv2.INTER_AREA)
        resized_path = os.path.join(output_dirs['resized'], image_name)
        if not cv2.imwrite(resized_path, resized):
            print(f"Gagal menyimpan resize gambar: {resized_path}")
    except Exception as e:
        print(f"Gagal melakukan resize pada gambar {image_name}: {e}")

    try:
        # Crop gambar
        cropped = image[50:300, 50:300]
        cropped_path = os.path.join(output_dirs['cropped'], image_name)
        if not cv2.imwrite(cropped_path, cropped):
            print(f"Gagal menyimpan crop gambar: {cropped_path}")
    except Exception as e:
        print(f"Gagal melakukan crop pada gambar {image_name}: {e}")

    try:
        # Flip gambar (horizontal)
        flipped = cv2.flip(image, 1)
        flipped_path = os.path.join(output_dirs['flipped'], image_name)
        if not cv2.imwrite(flipped_path, flipped):
            print(f"Gagal menyimpan flip gambar: {flipped_path}")
    except Exception as e:
        print(f"Gagal melakukan flip pada gambar {image_name}: {e}")

    try:
        # Rotate gambar 90 derajat searah jarum jam
        (h, w) = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, -90, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h))
        rotated_path = os.path.join(output_dirs['rotated'], image_name)
        if not cv2.imwrite(rotated_path, rotated):
            print(f"Gagal menyimpan rotate gambar: {rotated_path}")
    except Exception as e:
        print(f"Gagal melakukan rotasi pada gambar {image_name}: {e}")

    print(f"Berhasil memproses gambar: {image_name}")

print("Semua gambar telah diproses dan disimpan di direktori output.")
