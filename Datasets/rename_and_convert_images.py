import os
from PIL import Image
import re
Image.MAX_IMAGE_PIXELS = None  

def rename_and_convert_images(folder_path, prefix="image", target_ext=".jpg"):
    files = os.listdir(folder_path)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', 'avif'))]
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

        img = img.resize((256, 256), Image.Resampling.LANCZOS)

        counter += 1
        new_name = f"{prefix}_{counter}{target_ext}"
        dst = os.path.join(folder_path, new_name)
        img.save(dst)
        os.remove(src)  

    print(f"Updated {folder_path}: {counter - max_idx} new images converted & resized to 256x256.")

def count_total_images_except_test(root_dirs, test_folder="Test"):
    if isinstance(root_dirs, str):
        root_dirs = [root_dirs]

    total = 0
    for root_dir in root_dirs:
        for subdir, _, files in os.walk(root_dir):
            if test_folder.lower() in subdir.lower():  
                continue
            for f in files:
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.avif')):
                    total += 1
    print(f"Total imgs (not include {test_folder}): {total}")
    return total


rename_and_convert_images("Train/front", prefix="front", target_ext=".jpg")
rename_and_convert_images("Train/front_left", prefix="front_left", target_ext=".jpg")
rename_and_convert_images("Train/front_right", prefix="front_right", target_ext=".jpg")
rename_and_convert_images("Train/rear", prefix="rear", target_ext=".jpg")
rename_and_convert_images("Train/rear_left", prefix="rear_left", target_ext=".jpg")
rename_and_convert_images("Train/rear_right", prefix="rear_right", target_ext=".jpg")
rename_and_convert_images("Train/high_angle_view", prefix="high_angle_view", target_ext=".jpg")

rename_and_convert_images("Test/front", prefix="front", target_ext=".jpg")
rename_and_convert_images("Test/front_left", prefix="front_left", target_ext=".jpg")
rename_and_convert_images("Test/front_right", prefix="front_right", target_ext=".jpg")
rename_and_convert_images("Test/rear", prefix="rear", target_ext=".jpg")
rename_and_convert_images("Test/rear_left", prefix="rear_left", target_ext=".jpg")
rename_and_convert_images("Test/rear_right", prefix="rear_right", target_ext=".jpg")
rename_and_convert_images("Test/high_angle_view", prefix="high_angle_view", target_ext=".jpg")

count_total_images_except_test(root_dirs=["Train/front","Train/front_left","Train/front_right"
                                         "Train/rear","Train/rear_left","Train/rear_right","Train/high_angle_view"], test_folder="Test")