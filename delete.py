import os
import shutil

parent_path = r"D:\Users\azaan\Desktop\Sophie"



for i in range(3, 1001):
    folder_path = os.path.join(parent_path, f"Sophie {i}")

    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        print(f"Deleted: {folder_path}")

print("Done!")
