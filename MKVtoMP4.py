#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
file_list = []
ext_list = ['.flv', '.mkv']


def ffmpeg(input, output):
    os.system(r'D:\Software\MoviesMaker\ffmpeg\bin\ffmpeg.exe'+' -i '+input+' -vcodec copy -acodec copy -movflags faststart '+output)


def file_search(filepath):
    files = os.listdir(filepath)
    for file in files:
        file_join = os.path.join(filepath, file)
        if os.path.isdir(file_join):
            file_search(file_join)
        else:
            file_list.append(os.path.join(filepath, file_join))


file_search(os.getcwd())

for i in file_list:
    if os.path.splitext(i)[1] in ext_list:
        ffmpeg(i, os.path.splitext(i)[0]+'.mp4')
        os.remove(i)
