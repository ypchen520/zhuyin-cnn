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
import numpy as ny

_xml_root_dir = "../dataset-xml"
_img_root_dir = "../dataset-img"
_data_root_dir = "../cnn-pytorch/data/zmg"
_pid_pattern = "p\d{3}"
_canvas_size = 581
_x_offset = 0
_y_offset = 120
_target_size = 160

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
        print(dirpath)
        print(dirnames)
        # print(filenames)
        match = re.match(_pid_pattern, dirpath[-4:])
        if match:
            pid = dirpath[-4:]
            print(pid)
            # create a folder for pid
            img_folder_path = os.path.join(_img_root_dir, pid)
            print(img_folder_path)
            # os.makedirs(_data_root_dir, exist_ok=True)
            for filename in filenames:
                if filename == ".DS_Store":
                    continue
                # Use os.path.join to create the full file path
                file_path = os.path.join(dirpath, filename)
                img_filename = filename[:-3]+"png"
                # img = Image.fromarray(np.uint8(img_arr*255))
                img_file_path = os.path.join(img_folder_path, img_filename)
                cnt += 1
                # os.makedirs(img_file_path, exist_ok=True)
                # img.save(img_file_path)
    print(cnt)

if __name__ == "__main__":
    parse_and_draw()