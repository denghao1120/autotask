import time

import pyautogui
from pyautogui import *
from PIL import Image
import numpy as np
from paddleocr import PaddleOCR, draw_ocr


def get_curtime(time_format="%Y-%m-%d %H:%M:%S"):
    curTime = time.localtime()
    curTime = time.strftime(time_format, curTime)
    return curTime


def ocr_img_text(window, path="", saving=False):
    '''
    图像文字识别
    :param window: 指定需要截图的窗口
    :param path:图片路径
    :return:result
    '''
    image = path

    # 图片路径为空就默认获取屏幕截图
    if image == "":
        if window is not None:
            image = custom_screenshot(window)  # 使用pyautogui进行截图操作
        else:
            image = screenshot()  # 使用pyautogui进行截图操作
        image = np.array(image)
    else:
        # 不为空就打开
        image = Image.open(image).convert('RGB')
        image = np.array(image)  # 经提醒，需要添加array

    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory

    result = ocr.ocr(image, cls=True)

    # 识别出来的文字保存为图片
    if saving is True:
        img_name = "ImgTextOCR-img-" + get_curtime("%Y%m%d%H%M%S") + ".jpg"
        boxes = [detection[0] for line in result for detection in line]  # Nested loop added
        txts = [detection[1][0] for line in result for detection in line]  # Nested loop added
        scores = [detection[1][1] for line in result for detection in line]  # Nested loop added
        im_show = draw_ocr(image, boxes, txts, scores)
        im_show = Image.fromarray(im_show)
        im_show.save(img_name)

    return result, image


def get_location(data_info, text):
    '''
    匹配目标文本是否存在
    :param data_info:
    :param text:
    :return:
    '''
    for line in data_info:
        for word in line:
            if text in word[1][0]:
                return word
    return None





def get_centre(info, target_text):
    '''
    计算文本按钮的中心坐标
    :param info:  采集到的文本坐标信息
    :param target_text: 目标文本信息
    :return:
    '''
    tex = info[1][0]
    coords = info[0]
    if tex == target_text:
        x = info[0][0] + (info[2][0] - info[0][0]) / 2
    else:
        index = tex.find(target_text)
        end = index + len(target_text)
        w = coords[1][0] - coords[0][0]
        b = w * (index / len(tex))
        x = coords[0][0] + b + (w * (end / len(tex)) - b) / 2
    y = coords[0][1] + (coords[2][1] - coords[0][1]) / 2
    return x, y


def custom_screenshot(window):
    return pyautogui.screenshot(region=window.box)


if __name__ == "__main__":
    result = ocr_img_text()
    aa = get_location(result[0], "猪八戒")
    print(aa)
    centre = get_centre(aa, "猪八戒")
    print(centre)
    pyautogui.click(centre[0], centre[1], duration=0.5)
    # print(result, aa, centre)
