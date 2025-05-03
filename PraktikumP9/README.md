# Diskusi Modul 9: Representasi Video (Pemrosesan Citra Digital)

Modul ini membahas cara membaca, memproses, dan menyimpan video menggunakan OpenCV dalam konteks pemrosesan citra digital. Berikut adalah jawaban dari pertanyaan diskusi yang diberikan.

## 📌 1. Apa yang dimaksud dengan representasi video dalam konteks pemrosesan citra digital?

Representasi video adalah susunan berurutan dari frame (gambar diam) yang ditampilkan secara cepat untuk memberikan ilusi gerakan. Dalam konteks pemrosesan citra digital, representasi video digunakan untuk memanipulasi dan menganalisis video melalui frame-frame tersebut, misalnya untuk deteksi objek, tracking, atau ekstraksi informasi visual.

---

## 📌 2. Apa saja metadata yang dapat diekstrak dari sebuah video menggunakan OpenCV?

Metadata video yang dapat diakses menggunakan OpenCV meliputi:

- `cv2.CAP_PROP_FRAME_COUNT` → Jumlah total frame dalam video.
- `cv2.CAP_PROP_FPS` → Frame rate (jumlah frame per detik).
- `cv2.CAP_PROP_FRAME_WIDTH` → Lebar setiap frame (piksel).
- `cv2.CAP_PROP_FRAME_HEIGHT` → Tinggi setiap frame (piksel).
- `cv2.CAP_PROP_POS_MSEC` → Posisi waktu saat ini dalam milidetik.
- `cv2.CAP_PROP_POS_FRAMES` → Posisi frame saat ini.
  
Informasi ini penting untuk memahami struktur dan durasi video serta keperluan manipulasi lanjutan.

---

## 📌 3. Mengapa perlu dilakukan konversi warna dalam pemrosesan video?

Konversi warna dilakukan karena:

- **Efisiensi pemrosesan**: Misalnya, konversi ke grayscale mengurangi dimensi data dari 3 channel (RGB) ke 1 channel saja.
- **Kemudahan analisis**: Warna tertentu lebih mudah dianalisis dalam ruang warna HSV (Hue, Saturation, Value) dibanding RGB.
- **Penerapan algoritma**: Beberapa algoritma (seperti deteksi tepi, deteksi wajah, segmentasi warna) bekerja lebih optimal dalam representasi warna tertentu.

Dengan konversi warna, proses seperti deteksi objek, segmentasi, atau tracking dapat dilakukan dengan hasil lebih baik dan akurat.

---

