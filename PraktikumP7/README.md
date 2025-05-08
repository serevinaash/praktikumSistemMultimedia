# 🧪 Praktikum Sistem Multimedia – Pertemuan 7
## Analisis Frekuensi Audio menggunakan Fourier Transform

### 🎯 Tujuan Praktikum
- Memahami konsep Fourier Transform dalam domain audio.
- Menggunakan Python (Librosa dan NumPy) untuk menganalisis spektrum frekuensi audio.
- Menampilkan hasil visualisasi spektrum frekuensi.

---

## 📖 Diskusi

### 1. Apa manfaat utama dari melakukan analisis frekuensi pada sinyal audio?

Analisis frekuensi sangat penting karena memungkinkan kita mengetahui komponen frekuensi dominan dalam sinyal audio. Ini berguna dalam berbagai aplikasi seperti:
- **Pengenalan ucapan** (speech recognition)
- **Penyaringan suara** (filtering)
- **Kompresi data audio**
- **Deteksi noise atau anomali dalam suara**
- **Analisis pola atau karakteristik suara**

Fourier Transform membantu mengubah sinyal dari domain waktu ke domain frekuensi sehingga pola tersembunyi menjadi lebih mudah diidentifikasi.

---

### 2. Mengapa kita hanya menampilkan setengah dari spektrum frekuensi?

Fast Fourier Transform (FFT) pada sinyal real (seperti suara) menghasilkan spektrum frekuensi yang **simetris**. Artinya, bagian negatif dari spektrum hanyalah cerminan dari bagian positifnya, dan tidak memberikan informasi baru.

Karena itu, kita cukup menampilkan **setengah spektrum (frekuensi positif)** untuk mendapatkan gambaran lengkap dari distribusi frekuensinya.

---

### 3. Apakah ada perbedaan spektrum frekuensi antara suara manusia dan suara alat musik? Jelaskan.

Ya, ada perbedaan yang jelas antara keduanya:

- **Suara Manusia**:
  - Memiliki frekuensi dasar (fundamental) sekitar **85–255 Hz** tergantung jenis kelamin dan usia.
  - Mengandung **harmonik** dan **formant** khas yang mencerminkan bentuk saluran vokal.
  - Spektrum cenderung lebih **acak dan dinamis**.

- **Suara Alat Musik**:
  - Menampilkan **pola frekuensi yang lebih terstruktur dan periodik**.
  - Spektrum bisa lebih **luas dan konsisten**, tergantung pada jenis alat musik.
  - Setiap instrumen memiliki **tanda tangan frekuensi (timbre)** yang khas dan bisa dikenali dari pola spektrumnya.


