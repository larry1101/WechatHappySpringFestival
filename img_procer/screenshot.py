# -*- coding: utf-8 -*-
"""
手机屏幕截图的代码
"""
import subprocess
import os
import sys
from PIL import Image


# SCREENSHOT_WAY 是截图方法，经过 check_screenshot 后，会自动递减，不需手动修改
SCREENSHOT_WAY = 3

SCREENSHOT_NAME = 'screen_shot.png'


def pull_screenshot(file_name_append=''):
    """
    获取屏幕截图，目前有 0 1 2 3 四种方法，未来添加新的平台监测方法时，
    可根据效率及适用性由高到低排序
    """
    global SCREENSHOT_WAY
    if 1 <= SCREENSHOT_WAY <= 3:
        process = subprocess.Popen(
            'adb shell screencap -p',
            shell=True, stdout=subprocess.PIPE)
        binary_screenshot = process.stdout.read()
        if SCREENSHOT_WAY == 2:
            binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
        elif SCREENSHOT_WAY == 1:
            binary_screenshot = binary_screenshot.replace(b'\r\r\n', b'\n')
        f = open(SCREENSHOT_NAME+file_name_append, 'wb')
        f.write(binary_screenshot)
        f.close()
    elif SCREENSHOT_WAY == 0:
        os.system('adb shell screencap -p /sdcard/%s'%SCREENSHOT_NAME+file_name_append)
        os.system('adb pull /sdcard/%s .'%SCREENSHOT_NAME+file_name_append)


def check_screenshot():
    """
    检查获取截图的方式
    """
    global SCREENSHOT_WAY
    from adb_utils.adb_helper import ch_2_abd_dir
    ch_2_abd_dir()
    if os.path.isfile(SCREENSHOT_NAME):
        try:
            os.remove(SCREENSHOT_NAME)
        except Exception:
            pass
    if SCREENSHOT_WAY < 0:
        print('暂不支持当前设备')
        sys.exit()
    pull_screenshot()
    try:
        Image.open('./%s'%SCREENSHOT_NAME).load()
        # print('采用方式 {} 获取截图'.format(SCREENSHOT_WAY))
    except Exception:
        SCREENSHOT_WAY -= 1
        check_screenshot()
