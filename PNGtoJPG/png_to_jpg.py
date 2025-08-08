from PIL import Image
import os

# Path input & output
input_folder = r"D:\PNG_to_JPG\png"
output_folder = r"D:\PNG_to_JPG"

# Buat folder output kalau belum ada
os.makedirs(output_folder, exist_ok=True)

# Loop semua file PNG di folder input
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        # Buka gambar
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGBA")

        # Buat background putih
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])  # Pakai alpha channel

        # Simpan ke JPG dengan kualitas maksimal
        output_path = os.path.join(output_folder, filename.replace(".png", ".jpg"))
        background.save(output_path, "JPEG", quality=100)

print("✅ Konversi selesai tanpa kompres kualitas!")
