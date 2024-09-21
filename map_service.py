"""
@Project ：autotask 
@File    ：map_service.py
@Author  ：=等号=
@Description: 
@Date    ：2024/9/6 16:25 
"""

import pyautogui

from find_button import open_window


def open_map():
    pyautogui.hotkey("alt", "1")


def get_title_location():
    try:
        location = pyautogui.locateOnScreen("button/map_title.png", confidence=0.6)
        return location
    except pyautogui.ImageNotFoundException as e:
        print(f"the map  is not found")
    return None


def get_bottom_location():
    try:
        location = pyautogui.locateOnScreen("button/map_bottom.png", confidence=0.6)
        return location
    except pyautogui.ImageNotFoundException as e:
        print(f"the map  is not found")
    return None


def get_map_original_point():
    title = get_title_location()
    bottom = get_bottom_location()
    return title.left, bottom.top


def move_to(x, y, map_max_y):
    """
    移动到地图指定坐标，坐标和像素的比例  1:4
    :param x:
    :param y:
    :param map_max_y: 真实地图实际Y的最大值
    :return:
    """
    title = get_title_location()
    bottom = get_bottom_location()

    map_height = bottom.top - title.top - title.height  # 计算地图实际高度

    t = map_height / map_max_y  # 计算一个坐标值对应多少像素

    ox, oy = title.left, bottom.top
    pyautogui.moveTo(ox + x * t, oy - y * t)


if __name__ == "__main__":
    move_to(200, 100,  240)
