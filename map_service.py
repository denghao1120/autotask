"""
@Project ：autotask 
@File    ：map_service.py
@Author  ：=等号=
@Description: 
@Date    ：2024/9/6 16:25 
"""

import pyautogui

from find_button import open_window


# pyautogui.hotkey("alt", "tab")
#
#
# def get_map_size():
#     map1 = pyautogui.locateOnScreen("image/map.png", confidence=0.6)
#     return map1.width, map1.height
#
#
# def get_map_original_point(height):
#     map1 = pyautogui.locateOnScreen("image/title.png", confidence=0.6)
#     top = map1.top + map1.height
#     x = map1.left
#     y = top + height
#     return x, y


# width, height = get_map_size()


# def addressing(x, y):
#     ox, oy = get_map_original_point(height)
#     pyautogui.moveTo(ox + x, oy - y)


# addressing(100, 200)


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


def move_to(x, y):
    """
    移动到地图指定坐标，坐标和像素的比例  1:4
    :param x:
    :param y:
    :return:
    """
    ox, oy = get_map_original_point()
    print(ox, oy)
    pyautogui.moveTo(ox + x * 3.8, oy - y * 3.7)


if __name__ == "__main__":
    move_to(99, 22)
