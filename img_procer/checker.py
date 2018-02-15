from time import sleep

import numpy as np
from skimage import io

from img_procer.screenshot import pull_screenshot, SCREENSHOT_NAME

TITLE_BAR_GREEN_LINE = np.array([69, 192, 26, 255])


def check_title_bar_green_line():
    """
    检查title bar上搜索框的绿线
    :return: 有：true；没有：false
    """
    pull_screenshot()
    sc = io.imread(SCREENSHOT_NAME)
    if np.all(TITLE_BAR_GREEN_LINE == sc[190][540]):
        return True
    else:
        return False
