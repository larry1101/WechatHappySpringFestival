import os
from time import sleep

from operations.huawei_p9_plus import *


def _auto_sleep(auto_sleep_time=0.5):
    sleep(auto_sleep_time)


def tap(x, y):
    'adb shell input tap {x} {y}'.format(x=x, y=y)
    os.system(
        'adb shell input tap {x} {y}'.format(x=x, y=y))


def click_wechat_nav_contact():
    print('adb shell input tap {x} {y}'.format(x=WECHAT_NAVIGATION_CONTACT_X_CENTER, y=WECHAT_NAVIGATION_BAR_Y_CENTER))
    os.system(
        'adb shell input tap {x} {y}'.format(x=WECHAT_NAVIGATION_CONTACT_X_CENTER, y=WECHAT_NAVIGATION_BAR_Y_CENTER))


def click_wechat_nav_home():
    print('adb shell input tap {x} {y}'.format(x=WECHAT_NAVIGATION_HOME_X_CENTER, y=WECHAT_NAVIGATION_BAR_Y_CENTER))
    os.system(
        'adb shell input tap {x} {y}'.format(x=WECHAT_NAVIGATION_HOME_X_CENTER, y=WECHAT_NAVIGATION_BAR_Y_CENTER))


def click_wechat_title_bar_search(auto_sleep=True):
    print('adb shell input tap {x} {y}'.format(x=WECHAT_TITLE_BAR_SEARCH_X_CENTER, y=WECHAT_TITLE_BAR_Y_CENTER))
    os.system(
        'adb shell input tap {x} {y}'.format(x=WECHAT_TITLE_BAR_SEARCH_X_CENTER, y=WECHAT_TITLE_BAR_Y_CENTER))
    if auto_sleep:
        _auto_sleep()


def click_wechat_title_bar_search_cancel(auto_sleep=True):
    print('adb shell input tap {x} {y}'.format(x=WECHAT_TITLE_BAR_SEARCH_CANCEL_X_CENTER, y=WECHAT_TITLE_BAR_Y_CENTER))
    os.system(
        'adb shell input tap {x} {y}'.format(x=WECHAT_TITLE_BAR_SEARCH_CANCEL_X_CENTER, y=WECHAT_TITLE_BAR_Y_CENTER))
    if auto_sleep:
        _auto_sleep()


def click_wechat_title_bar_back(auto_sleep=True):
    print('adb shell input tap {x} {y}'.format(x=WECHAT_TITLE_BAR_BACK_X_CENTER, y=WECHAT_TITLE_BAR_Y_CENTER))
    os.system(
        'adb shell input tap {x} {y}'.format(x=WECHAT_TITLE_BAR_BACK_X_CENTER, y=WECHAT_TITLE_BAR_Y_CENTER))
    if auto_sleep:
        _auto_sleep()


def click_shortcut(shortcut_name):
    _sc_index = CONTACT_SHORTCUTS[shortcut_name]
    _y_center = int(CONTACT_SHORTCUT_Y_TOP + CONTACT_SHORTCUT_ITEM_HEIGHT * (_sc_index + 0.5))
    cmd = 'adb shell input tap {x} {y}'.format(x=CONTACT_SHORTCUT_X_CENTER, y=_y_center)
    print(cmd)
    os.system(cmd)


def swipe_up(dy=None, swipe_time=None):
    if dy is None:
        if swipe_time is None:
            swipe_time = 2500
        cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {swipe_time}'.format(
            x1=X_CENTER,
            y1=CONTACT_SWIPE_UP_DEFAULT_Y_START,
            x2=X_CENTER,
            y2=CONTACT_SWIPE_UP_DEFAULT_Y_STOP + 18,
            swipe_time=swipe_time
        )
        print(cmd)
        os.system(cmd)
    else:
        if swipe_time is None:
            swipe_time = 1000
        cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {swipe_time}'.format(
            x1=X_CENTER,
            y1=CONTACT_SWIPE_UP_DEFAULT_Y_START,
            x2=X_CENTER,
            y2=CONTACT_SWIPE_UP_DEFAULT_Y_START - dy,
            swipe_time=swipe_time
        )
        print(cmd)
        os.system(cmd)


def swipe_up_a_sep():
    swipe_up(CONTACT_SEP_HEIGHT + 17, 500)
