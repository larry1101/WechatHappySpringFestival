import os

ADB_DIR = r'E:\Python Projects\WechatHappySpringFestival\Tools'
AS_ADB_DIR = r'D:\ASSDK\sdk\platform-tools'
ADB_CONNECT = False


def ch_2_abd_dir():
    # os.chdir(AS_ADB_DIR)
    os.chdir(ADB_DIR)


def tap(x, y):
    os.system("adb shell input tap %d %d" % (x, y))
