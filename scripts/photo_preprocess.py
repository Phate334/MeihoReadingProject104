# -*- coding: utf-8 -*-
import os, sys
import Image

import tinify

# https://tinypng.com/developers
# 必須事先申請 tinypng 的 API key或找前任助理。
tinify.key = ""

input_dir = "gallery"  # 原始圖檔輸入目錄
compress_dir = "compress"  #　壓縮圖檔輸出目錄
thumbnail_dir = "thumb"  # 縮圖書出目錄

out_wdith = 300
out_height = 200

if not os.path.isdir(compress_dir):
    os.makedirs(compress_dir)

if not os.path.isdir(thumbnail_dir):
    os.makedirs(thumbnail_dir)

def resize(target,out_dir):
    """return: Image instance,or None if open fail.
    """
    try:
        im = Image.open(target)
    except IOError:
        return None
    im = im.resize((out_wdith, out_height))
    split_name = list(os.path.splitext(os.path.basename(target)))
    split_name.insert(-1, "_m")
    filename = "".join(split_name)
    im.save(os.path.join(out_dir,filename))
    return im

if __name__ == "__main__":
    for img in os.listdir(input_dir):
        print(img)
        tinify.from_file(os.path.join(input_dir, img)).to_file(os.path.join(compress_dir, img))
    
    for img in os.listdir(compress_dir):
        resize(os.path.join(compress_dir, img), thumbnail_dir)
