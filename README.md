# AI Virtual Mouse Control

Proyek ini adalah aplikasi kontrol mouse virtual menggunakan kecerdasan buatan (AI) berbasis pengenalan tangan. Aplikasi ini memungkinkan pengguna untuk menggerakkan kursor mouse dan melakukan klik hanya dengan menggunakan gerakan tangan di depan webcam.
<img width="1201" height="613" alt="Cuplikan layar 2026-03-31 095949" src="https://github.com/user-attachments/assets/8b3a8854-fb72-4a57-82cb-4c820bdbd4f8" />

## Fitur
- **Kontrol Kursor**: Gerakkan kursor mouse dengan menggerakkan jari telunjuk Anda.
- **Klik Kiri**: Lakukan klik kiri dengan mendekatkan ujung jari telunjuk dan ujung ibu jari.
- **Visualisasi Real-time**: Menampilkan feed kamera dengan penanda (landmarks) tangan untuk memudahkan penggunaan.

## Syarat Sistem
Pastikan Anda memiliki Python terinstal di sistem Anda. Proyek ini menggunakan beberapa library eksternal yang perlu diinstal.

## Instalasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/esnpendosa/aimousecontrol.git
   cd aimousecontrol
   ```

2. Instal dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan aplikasi:
   ```bash
   python main.py
   ```

## Cara Penggunaan
- **Gerakkan Mouse**: Arahkan jari telunjuk Anda ke kamera. Kursor mouse akan mengikuti posisi jari telunjuk Anda di layar.
- **Klik**: Satukan ujung jari telunjuk dan ibu jari untuk melakukan klik kiri.
- **Keluar**: Tekan tombol `q` pada jendela kamera untuk menghentikan aplikasi.

## Dependensi Utama
- **OpenCV**: Untuk menangkap dan mengolah feed video dari webcam.
- **MediaPipe**: Untuk deteksi dan pelacakan landmark tangan secara akurat.
- **PyAutoGUI**: Untuk mengontrol pergerakan kursor dan aksi mouse secara programatik.

---
Dibuat dengan ❤️ untuk kemudahan interaksi manusia dan komputer.
