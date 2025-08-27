import shutil
import os


# Source (where kagglehub put it)
src = r"C:\Users\HP\.cache\kagglehub\datasets\paultimothymooney\chest-xray-pneumonia\versions\2"

# Destination (your preferred folder)
dst = r"D:\kaggle_datasets\chest-xray-pneumonia"

# Make sure destination directory exists
os.makedirs(os.path.dirname(dst), exist_ok=True)

# Copy entire folder
shutil.copytree(src, dst, dirs_exist_ok=True)

print("Dataset moved to:", dst)
