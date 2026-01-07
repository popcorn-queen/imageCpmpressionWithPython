
from PIL import Image
import os

input_folder = "images"
output_folder = "compressed_images"
quality = 70

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            img.save(output_path, "JPEG", quality=quality, optimize=True)

        print(f"Compressed: {filename}")
