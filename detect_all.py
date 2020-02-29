# -*-coding: utf-8-*-
# Author: AIBC-MrH
'''
批量测试检测图片
'''

import os
from yolo import YOLO
from PIL import Image


def detect_img(yolo):
    pic_temp = []
    pic = os.listdir(test_dir)
    for name in pic:
        pic_temp.append(name)
    for i in range(len(pic_temp)):
        img = test_dir + '/' + pic_temp[i]
        image = Image.open(img)
        detect = yolo.detect_image(image)
        # detect.show()
        detect.save(target_dir + '/' + pic_temp[i])
    yolo.close_session()
    return detect


if __name__ == '__main__':
    test_dir = './test_img'
    target_dir = './detect_results'
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    detect_img(YOLO())
