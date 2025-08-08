# PNG to JPG Converter with White Background

Script ini digunakan untuk mengonversi semua file PNG di folder input menjadi JPG dengan latar belakang warna putih tanpa mengompres kualitas gambar.

## Fitur
- Mengonversi PNG ke JPG
- Menambahkan latar belakang putih untuk menghilangkan transparansi
- Mempertahankan kualitas asli (quality=100)

## Struktur Folder
```
D:\PNG_to_JPG
├── png\ # Folder input file PNG
├── jpg\ # Folder output file JPG
└── png_to_jpg.py # Script Python
```

## Cara Menjalankan
1. Pastikan **Python** sudah terinstal di komputer.
2. Install library **Pillow**:
```
pip install pillow
```
Simpan script Python convert_png_to_jpg.py di mana saja (misal di Desktop).

Jalankan script:
```
python convert_png_to_jpg.py
