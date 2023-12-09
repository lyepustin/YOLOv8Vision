from pathlib import Path
import pyautogui
import numpy as np
import PIL.ImageOps
from numpy.random import uniform
from time import sleep, time
import soundcard as sc
import soundfile as sf
import matplotlib.pyplot as plt
import cv2
import sys

from PIL import Image
from PIL import ImageEnhance

import pytesseract
import re
import os


dict = {
    "01.png": {
        "box_x_left": "1299",
        "box_y_top": "530",
        "box_width": "36",
        "box_height": "34",
    },
    "02.png": {
        "box_x_left": "1229",
        "box_y_top": "531",
        "box_width": "34",
        "box_height": "26",
    },
    "03.png": {
        "box_x_left": "1238",
        "box_y_top": "602",
        "box_width": "33",
        "box_height": "28",
    },
    "04.png": {
        "box_x_left": "1241",
        "box_y_top": "576",
        "box_width": "23",
        "box_height": "23",
    },
    "05.png": {
        "box_x_left": "1315",
        "box_y_top": "368",
        "box_width": "30",
        "box_height": "24",
    },
    "06.png": {
        "box_x_left": "1288",
        "box_y_top": "669",
        "box_width": "34",
        "box_height": "28",
    },
    "07.png": {
        "box_x_left": "1299",
        "box_y_top": "501",
        "box_width": "32",
        "box_height": "23",
    },
    "08.png": {
        "box_x_left": "1226",
        "box_y_top": "468",
        "box_width": "24",
        "box_height": "20",
    },
    "09.png": {
        "box_x_left": "1256",
        "box_y_top": "310",
        "box_width": "27",
        "box_height": "25",
    },
    "10.png": {
        "box_x_left": "1314",
        "box_y_top": "628",
        "box_width": "41",
        "box_height": "33",
    },
    "11.png": {
        "box_x_left": "1181",
        "box_y_top": "589",
        "box_width": "34",
        "box_height": "30",
    },
    "12.png": {
        "box_x_left": "1049",
        "box_y_top": "674",
        "box_width": "36",
        "box_height": "26",
    },
    "13.png": {
        "box_x_left": "718",
        "box_y_top": "777",
        "box_width": "34",
        "box_height": "29",
    },
    "14.png": {
        "box_x_left": "1260",
        "box_y_top": "512",
        "box_width": "26",
        "box_height": "24",
    },
    "15.png": {
        "box_x_left": "1324",
        "box_y_top": "562",
        "box_width": "40",
        "box_height": "31",
    },
    "16.png": {
        "box_x_left": "1213",
        "box_y_top": "402",
        "box_width": "35",
        "box_height": "26"
    },
    "17.png": {
        "box_x_left": "1306",
        "box_y_top": "512",
        "box_width": "29",
        "box_height": "28"
    },
    "18.png": {
        "box_x_left": "1228",
        "box_y_top": "571",
        "box_width": "33",
        "box_height": "26"
    },
    "19.png": {
        "box_x_left": "1309",
        "box_y_top": "457",
        "box_width": "27",
        "box_height": "22"
    },
    "20.png": {
        "box_x_left": "1267",
        "box_y_top": "492",
        "box_width": "33",
        "box_height": "25"
    },
    "21.png": {
        "box_x_left": "1283",
        "box_y_top": "662",
        "box_width": "29",
        "box_height": "31"
    },
    "22.png": {
        "box_x_left": "1109",
        "box_y_top": "532",
        "box_width": "29",
        "box_height": "25"
    },
    "23.png": {
        "box_x_left": "1253",
        "box_y_top": "528",
        "box_width": "30",
        "box_height": "27"
    },
    "24.png": {
        "box_x_left": "1236",
        "box_y_top": "497",
        "box_width": "31",
        "box_height": "25"
    },
    "25.png": {
        "box_x_left": "1232",
        "box_y_top": "530",
        "box_width": "34",
        "box_height": "26"
    },
    "26.png": {
        "box_x_left": "1280",
        "box_y_top": "525",
        "box_width": "34",
        "box_height": "27"
    },
    "27.png": {
        "box_x_left": "1301",
        "box_y_top": "602",
        "box_width": "38",
        "box_height": "30"
    },
    "28.png": {
        "box_x_left": "1180",
        "box_y_top": "418",
        "box_width": "40",
        "box_height": "34"
    },
    "29.png": {
        "box_x_left": "1173",
        "box_y_top": "480",
        "box_width": "39",
        "box_height": "31"
    },
    "30.png": {
        "box_x_left": "1199",
        "box_y_top": "440",
        "box_width": "30",
        "box_height": "26"
    },
    "31.png": {
        "box_x_left": "1198",
        "box_y_top": "465",
        "box_width": "34",
        "box_height": "30"
    },
    "32.png": {
        "box_x_left": "1255",
        "box_y_top": "415",
        "box_width": "38",
        "box_height": "33"
    },
    "33.png": {
        "box_x_left": "1154",
        "box_y_top": "530",
        "box_width": "32",
        "box_height": "26"
    },
    "34.png": {
        "box_x_left": "1355",
        "box_y_top": "392",
        "box_width": "31",
        "box_height": "27"
    },
    "35.png": {
        "box_x_left": "1288",
        "box_y_top": "391",
        "box_width": "32",
        "box_height": "27"
    },
    "36.png": {
        "box_x_left": "1287",
        "box_y_top": "405",
        "box_width": "30",
        "box_height": "27"
    },
    "37.png": {
        "box_x_left": "1253",
        "box_y_top": "546",
        "box_width": "30",
        "box_height": "24"
    },
    "38.png": {
        "box_x_left": "1251",
        "box_y_top": "546",
        "box_width": "31",
        "box_height": "24"
    },
    "39.png": {
        "box_x_left": "1243",
        "box_y_top": "541",
        "box_width": "30",
        "box_height": "27"
    },
    "40.png": {
        "box_x_left": "1327",
        "box_y_top": "508",
        "box_width": "28",
        "box_height": "26"
    },
    "41.png": {
        "box_x_left": "1284",
        "box_y_top": "623",
        "box_width": "31",
        "box_height": "33"
    },
    "42.png": {
        "box_x_left": "1230",
        "box_y_top": "540",
        "box_width": "26",
        "box_height": "29"
    },
    "43.png": {
        "box_x_left": "1190",
        "box_y_top": "512",
        "box_width": "32",
        "box_height": "29"
    },
    "44.png": {
        "box_x_left": "1265",
        "box_y_top": "326",
        "box_width": "31",
        "box_height": "27"
    },
    "45.png": {
        "box_x_left": "1271",
        "box_y_top": "452",
        "box_width": "33",
        "box_height": "28"
    },
    "46.png": {
        "box_x_left": "1340",
        "box_y_top": "393",
        "box_width": "32",
        "box_height": "26"
    },
    "47.png": {
        "box_x_left": "1215",
        "box_y_top": "309",
        "box_width": "27",
        "box_height": "24"
    },
    "48.png": {
        "box_x_left": "880",
        "box_y_top": "442",
        "box_width": "21",
        "box_height": "19"
    },
    "49.png": {
        "box_x_left": "890",
        "box_y_top": "278",
        "box_width": "24",
        "box_height": "20"
    },
    "50.png": {
        "box_x_left": "892",
        "box_y_top": "429",
        "box_width": "27",
        "box_height": "21"
    },
    "51.png": {
        "box_x_left": "885",
        "box_y_top": "364",
        "box_width": "28",
        "box_height": "20"
    },
    "52.png": {
        "box_x_left": "942",
        "box_y_top": "402",
        "box_width": "22",
        "box_height": "18"
    },
    "53.png": {
        "box_x_left": "946",
        "box_y_top": "415",
        "box_width": "21",
        "box_height": "17"
    },
    "54.png": {
        "box_x_left": "1000",
        "box_y_top": "380",
        "box_width": "19",
        "box_height": "18"
    },
    "55.png": {
        "box_x_left": "1297",
        "box_y_top": "507",
        "box_width": "29",
        "box_height": "24"
    }
}

if __name__ == "__main__":
    for screen_file in os.listdir(Path(r"data/tests")):
        if screen_file.endswith(".png"):
            img_rgb = cv2.imread(os.path.join(Path(r"data/tests"), screen_file))
            image_height, image_width, _ = img_rgb.shape
            
            box_x_left = int(dict[screen_file]["box_x_left"])
            box_y_top = int(dict[screen_file]["box_y_top"])
            box_width = int(dict[screen_file]["box_width"])
            box_height = int(dict[screen_file]["box_height"])  
            
            x_center = (box_x_left + box_width/2)/image_width
            y_center = (box_y_top + box_height/2)/image_height
            width = box_width/image_width
            height = box_height/image_height

            object_class_id = "bobber"
            
            cv2.imwrite(os.path.join(Path(r"data/train/images"), screen_file), img_rgb)

            txt_screen_file = screen_file.replace(".png", ".txt")
            with open(os.path.join(Path(r"data/train/labels"), txt_screen_file), 'w') as file:
                file.write(f"{object_class_id} {x_center} {y_center} {width} {height}")
