import os
from PIL import Image
import re

def rename_and_convert_images(folder_path, prefix="image", target_ext=".jpg"):
    files = os.listdir(folder_path)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    image_files.sort()

    pattern = re.compile(rf"^{prefix}_(\d+){re.escape(target_ext)}$", re.IGNORECASE)

    max_idx = 0
    for f in image_files:
        m = pattern.match(f)
        if m:
            idx = int(m.group(1))
            if idx > max_idx:
                max_idx = idx

    counter = max_idx
    for filename in image_files:
        if pattern.match(filename):  
            continue

        src = os.path.join(folder_path, filename)
        img = Image.open(src).convert("RGB")

        counter += 1
        new_name = f"{prefix}_{counter}{target_ext}"
        dst = os.path.join(folder_path, new_name)
        img.save(dst)
        os.remove(src)  

    print(f"Updated {folder_path}: {counter - max_idx} new images converted.")

rename_and_convert_images("front", prefix="front", target_ext=".jpg")
rename_and_convert_images("front_left", prefix="front_left", target_ext=".jpg")
rename_and_convert_images("front_right", prefix="front_right", target_ext=".jpg")
rename_and_convert_images("rear", prefix="rear", target_ext=".jpg")
rename_and_convert_images("rear_left", prefix="rear_left", target_ext=".jpg")
rename_and_convert_images("rear_right", prefix="rear_right", target_ext=".jpg")
rename_and_convert_images("high_angle_view", prefix="high_angle_view", target_ext=".jpg")
