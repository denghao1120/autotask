"""
@Project ：autotask 
@File    ：game.py
@Author  ：=等号=
@Description: 
@Date    ：2024/9/21 15:00 
"""
import pyautogui
import re


def block_players():
    # 屏蔽所有玩家
    pyautogui.hotkey("alt", "4")


def block_stall():
    # 屏蔽摊位
    pyautogui.hotkey("alt", "5")


def auto_battle():
    # 自动战斗
    pyautogui.hotkey("alt", "8")


def is_in_battle(data_infos) -> bool:
    '''
    通过判断是否存在  洛阳城［157,40］  格式的字符串判断是否是在战斗状态下
    :param text:
    :return:
    '''
    pattern = r'^[^\[\]]+\[\d+，\d+\]'
    for data in data_infos:
        tex = data[1][0]
        if tex is None or tex == "":
            continue
        flag = bool(re.match(pattern, tex))
        if flag:
            print(tex)
            return False
    return True


def has_auto_battle(data_infos) -> bool:
    pattern = r'.+自动还剩余\d+回合.+'
    for data in data_infos:
        tex = data[1][0]
        if tex is None or tex == "":
            continue
        flag = bool(re.match(pattern, tex))
        if flag:
            print(tex)
            return True
    return False
