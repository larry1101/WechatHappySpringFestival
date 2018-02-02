import os
import random
from time import sleep
from warnings import warn

from adb_utils.adb_helper import ch_2_abd_dir

ch_2_abd_dir()


def input_text(adb_str):
    if ' ' in adb_str:
        raise Exception('不支持空格')
    print("adb shell am broadcast -a ADB_INPUT_TEXT --es msg {input_text} ".format(input_text=adb_str))
    os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg {input_text} ".format(input_text=adb_str))


def backspace(n=1):
    for i in range(n):
        os.system("adb shell input keyevent 67")
        sleep(random.uniform(0.1, 0.2))


def enter(n=1):
    for i in range(n):
        os.system("adb shell input keyevent 66")
        sleep(random.uniform(0.1, 0.2))


def keyevent(keyevent_code=None):
    if keyevent_code is None:
        warn('No Keyevent!')
        return
    os.system("adb shell input keyevent %d" % keyevent_code)


def left(n=1):
    for i in range(n):
        os.system("adb shell input keyevent 21")
        sleep(random.uniform(0.1, 0.2))


def right(n=1):
    for i in range(n):
        os.system("adb shell input keyevent 22")
        sleep(random.uniform(0.1, 0.2))


def back(n=1):
    for i in range(n):
        os.system("adb shell input keyevent 4")
        sleep(random.uniform(0.1, 0.2))


def home():
    os.system("adb shell input keyevent 3")
