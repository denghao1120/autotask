import time

import pyautogui

import game
from find_button import open_window
from parse_images import ocr_img_text

# pyautogui.mouseInfo()


if __name__ == "__main__":
    win = open_window("大话西游")
    time.sleep(0.2)
    result = ocr_img_text(win, saving=True)

    in_battle = game.is_in_battle(result[0][0][:10])
    print("是否是在战斗状态：", in_battle)

    if in_battle:
        f = game.has_auto_battle(result[0][0][:10])
        print("是否还在自动战斗状态：", f)
        if not f:
            game.auto_battle()
            print("切换为自动战斗")

    # print(result)
