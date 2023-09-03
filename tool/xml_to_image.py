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

_xml_kj_root_dir = "../dataset-kj-xml"
_xml_root_dir = "../dataset-xml"
_img_root_dir = "../dataset-img"
_pid_pattern = "p\d{3}"
_canvas_size = 581
_x_offset = 0
_y_offset = 120
_target_size = 160
_dirs = [[0,1],[1,0],[0,-1],[-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]

def is_valid(x, y, width, height):
    return x >= 0 and x < width and y >= 0 and y < height

def find_canvas_dims():
    cnt = 0
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for dirpath, dirnames, filenames in os.walk(_xml_kj_root_dir):
        # Loop through the filenames and print their full paths
        match = re.match(_pid_pattern, dirpath[-4:])
        if match:
            pid = dirpath[-4:]
            # create a folder for pid
            img_folder_path = os.path.join(_img_root_dir, pid)
            print(img_folder_path)
            os.makedirs(img_folder_path, exist_ok=True)
            for filename in filenames:
                if filename == ".DS_Store":
                    continue
                file_path = os.path.join(dirpath, filename)
                tree = etree.parse(file_path)
                xml_string = etree.tostring(tree, pretty_print=True)
                gesture_ele = etree.fromstring(xml_string)
                gesture_attr = gesture_ele.attrib
                # "Name" for gesture name: NAME~'{:02}'.format(i)
                # img_file_path = os.path.join(_img_root_dir, filename[:-3])
                img_filename = filename[:-3]+"png"
                img_file_path = os.path.join(img_folder_path, img_filename)
                # each image
                for stroke_ele in gesture_ele.iterchildren():
                    # stroke_ele.attrib['index']
                    for point_ele in stroke_ele.iterchildren():
                        x = int(point_ele.attrib['X'])
                        y = int(point_ele.attrib['Y'])
                        max_x, max_y, min_x, min_y = max(max_x, x), max(max_y, y), min(min_x, x), min(min_y, y)
                cnt += 1
    print(cnt)
    # return max_x-min_x+1, max_y-min_y+1
    return max_x, max_y, min_x, min_y

def parse_and_draw(offsets, dims):
    x_offset = offsets[0]
    y_offset = offsets[1]
    width = dims[0]
    height = dims[1]
    if dims[0] != dims[1]:
        width = height = max(dims[0], dims[1])
    cnt = 0
    for dirpath, dirnames, filenames in os.walk(_xml_kj_root_dir):
        # Loop through the filenames and print their full paths
        match = re.match(_pid_pattern, dirpath[-4:])
        if match:
            pid = dirpath[-4:]
            # create a folder for pid
            img_folder_path = os.path.join(_img_root_dir, pid)
            # print(img_folder_path)
            os.makedirs(img_folder_path, exist_ok=True)
            for filename in filenames:
                # create the image
                img_arr = np.zeros((width, height, 3))
                # img_arr = np.zeros((_canvas_size, _canvas_size))
                if filename == ".DS_Store":
                    continue
                # Use os.path.join to create the full file path
                file_path = os.path.join(dirpath, filename)
                tree = etree.parse(file_path)
                xml_string = etree.tostring(tree, pretty_print=True)
                gesture_ele = etree.fromstring(xml_string)
                gesture_attr = gesture_ele.attrib
                # "Name" for gesture name: NAME~'{:02}'.format(i)
                # img_file_path = os.path.join(_img_root_dir, filename[:-3])
                img_filename = filename[:-3]+"png"
                img_file_path = os.path.join(img_folder_path, img_filename)
                # each image
                for stroke_ele in gesture_ele.iterchildren():
                    # stroke_ele.attrib['index']
                    for point_ele in stroke_ele.iterchildren():
                        x = int(point_ele.attrib['X']) - x_offset
                        # y = int(point_ele.attrib['Y']) - _y_offset
                        y = int(point_ele.attrib['Y']) - y_offset
                        img_arr[y][x][:] = 1
                        # img_arr[y][x] = 1
                        for dir in _dirs:
                            nx = x+dir[0]
                            ny = y+dir[1]
                            nnx = x+dir[0]*2
                            nny = y+dir[1]*2
                            if is_valid(nx, ny, width, height):
                                img_arr[ny][nx][:] = 1
                                # img_arr[ny][nx] = 1
                            if is_valid(nnx, nny, width, height):
                                img_arr[nny][nnx][:] = 1
                img = Image.fromarray(np.uint8(img_arr*255))
                img = img.resize((_canvas_size, _canvas_size), Image.Resampling.LANCZOS)
                # img_arr = np.array(img)
                # nonzero_pixels = np.argwhere(img_arr==255)
                # min_row, min_col = np.min(nonzero_pixels, axis=0)
                # max_row, max_col = np.max(nonzero_pixels, axis=0)

                # char_height = max_row - min_row + 1
                # char_width = max_col - min_col + 1

                # aspect_ratio = char_width / char_height

                # max_dim = max(char_height, char_width)

                # new_width = int(max_dim * aspect_ratio)
                # new_height = int(max_dim)

                # resized_gesture = img.crop((min_row, min_col, max_row+1, max_col+1))
                # resized_gesture = resized_gesture.resize((new_width, new_height), Image.ANTIALIAS)

                # new_img = Image.new("L", (max_dim, max_dim), 0)

                # x_offset = (max_dim - new_width) // 2
                # y_offset = (max_dim - new_height) // 2

                # new_img.paste(resized_gesture, (x_offset, y_offset))

                # new_img.save(img_file_path)

                cnt += 1
                # os.makedirs(img_file_path, exist_ok=True)
                img.save(img_file_path)
    print(cnt)

if __name__ == "__main__":
    max_x, max_y, min_x, min_y = find_canvas_dims()
    # print(max_x, max_y, min_x, min_y)
    # parse_and_draw((_x_offset, _y_offset), (_canvas_size, _canvas_size)) # dataset-xml
    parse_and_draw((min_x, min_y), (max_x-min_x+1, max_y-min_y+1)) # dataset-kj-xml