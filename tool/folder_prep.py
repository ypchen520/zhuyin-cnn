"""
- original canvas size:
    - 500 * 580
- offset
    - (0,120)
    - (500,700)
- target image size:
    - 160 * 160
"""

import os
import re
from lxml import etree
import numpy as np
from PIL import Image
import random
import shutil

_img_root_dir = "../dataset-img"
_data_root_dir = "../cnn-pytorch/data/zmg"
_pid_pattern = "p\d{3}"
_num_classes = 16

def parse_and_draw():
    """
    1. get pid
    2. go into the folder of pid
    3. append pid to the end of each gesture filename
    4. create a folder for each class in zmg/train and zmg/val
    5. put the gesture image in the corresponding folder, e.g., zmg/train/b/b01-p001.png
    6. make sure zmg/val contains gesture from each P (randomly), e.g., zmg/val/b/b09-p001.png, zmg/val/b/b05-p006.png, 
    """
    cnt = 0
    for dirpath, dirnames, filenames in os.walk(_img_root_dir):
        # Loop through the filenames and print their full paths
        # print(dirpath)
        # print(dirnames)
        # print(filenames)
        match = re.match(_pid_pattern, dirpath[-4:])
        if match:
            pid = dirpath[-4:]
            # get a list of random integer for train/val 
            val_labels = {}
            for filename in filenames:
                if filename == ".DS_Store":
                    continue
                filename = filename.split(".")[0] # remove .png
                label = filename[:-2] # get class label
                index = filename[-2:]
                
                # create a folder in train/ and val/ for each label
                train_folder_path = os.path.join(_data_root_dir, "train", label)
                val_folder_path = os.path.join(_data_root_dir, "val", label)
                os.makedirs(train_folder_path, exist_ok=True)
                os.makedirs(val_folder_path, exist_ok=True)

                img_filename = filename+".png"
                img_file_path = os.path.join(dirpath, img_filename)
                # print(img_file_path)

                # For each label, decide the ix that will be used for val first
                if label not in val_labels:
                    ix = random.randint(1,10)
                    val_labels[label] = f"{ix:0{2}d}"

                dst_img_filename = "-".join([filename,pid])+".png"
                if index != val_labels[label]:
                    # indices for training data
                    dst_img_file_path = os.path.join(train_folder_path, dst_img_filename)
                else:
                    # index for val data
                    dst_img_file_path = os.path.join(val_folder_path, dst_img_filename)
                shutil.copy(img_file_path, dst_img_file_path)
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    parse_and_draw()