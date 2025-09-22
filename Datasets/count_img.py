import os

def count_images_in_folder(folders, exts=(".jpg", ".jpeg", ".png")):
    counts = {}
    for folder in folders:
        if not os.path.exists(folder):
            print(f"[WARN] Folder not found: {folder}")
            counts[folder] = 0
            continue

        files = [
            f for f in os.listdir(folder)
            if f.lower().endswith(exts)
        ]
        counts[folder] = len(files)

    return counts

folders = [
    "Train/front",
    "Train/front_left",
    "Train/front_right",
    "Train/rear",
    "Train/rear_left",
    "Train/rear_right",
    "Train/high_angle_view"
]

result = count_images_in_folder(folders)
print("Number images for each folder:")
for k, v in result.items():
    print(f"{k}: {v}")
print(f"Total images: {sum(result.values())}")