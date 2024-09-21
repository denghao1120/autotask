"""
@Project ：autotask 
@File    ：find_button.py
@Author  ：=等号=
@Description: 
@Date    ：2024/9/17 15:39 
"""
import pyautogui


def find_button(button_img_path):
    """
    寻找按钮所在位置
    :param button_img_path: 按钮图标样例路径
    :return:
    """
    try:
        location = pyautogui.locateOnScreen(button_img_path, confidence=0.6)
        return pyautogui.center(location)
    except pyautogui.ImageNotFoundException as e:
        print(f"the button is not found: {button_img_path}")
    return None


def click_button(button_img_path):
    """
    点击按钮
    :param button_img_path: 按钮图标样例路径
    :return:
    """
    button = find_button(button_img_path)
    if button:
        pyautogui.click(button)


def open_window(window_title):
    """
    根据窗口title打开窗口
    :return:
    """
    # 获取所有窗口的标题
    all_titles = pyautogui.getAllTitles()

    # 假设要打开的窗口标题为特定标题
    for t in all_titles:
        if window_title in t:
            window = pyautogui.getWindowsWithTitle(t)[0]
            window.activate()
            return window

    print(f"未找到标题为'{window_title}'的窗口。")


def open_window_use_image(image_path):
    """
    根据图片打开窗口
    :param image_path:
    :return:
    """
    click_button(image_path)


if __name__ == "__main__":
    win = open_window("大话西游")
    print(win)
    # 打开任务窗口
    click_button("button/task_butten.png")
    # 关闭任务窗口
    click_button("button/close1.png")
