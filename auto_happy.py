from time import sleep

from adb_utils.adb_helper import ch_2_abd_dir
from adb_utils.adb_inputter import input_text
from greeting_procer.procer import load_greetings
from operations.oper import *

print('初始化')
ch_2_abd_dir()
sleep(0.1)

print('============================================')
print('                 问候')

start_config = input('请确认在微信的主界面并且输入法已调至ADB IME/ADB Keyboard\n确认开始? (输入y) \n 否则输入任意其他字符\n')
if start_config != 'y':
    print('再见')
    exit(-1)
print('============================================')

click_wechat_nav_home()

sleep(0.5)

click_wechat_title_bar_search()

contacts = load_greetings(r'E:\Python Projects\WechatHappySpringFestival\greetings\sf.xlsx')

for each_contact in contacts:
    print('-----------------------------------------------')
    print('              对 {somebody} 问候'.format(somebody=each_contact))
    input_text(each_contact)
    sleep(0.7)
    tap(X_CENTER, MATCH_CONTACT_1_Y_CENTER)
    sleep(0.5)
    tap(540, INPUT_EDITOR_Y_CENTER)
    for each_greet in contacts[each_contact]:
        input_text(each_greet[1])
        sleep(0.5)
        tap(990, INPUT_EDITOR_Y_CENTER - ADB_IME_HEIGHT)
        sleep(0.5)
        # backspace(3)
    click_wechat_title_bar_back()
    click_wechat_title_bar_search_cancel()
    print('-----------')
    print('         完成了对 {somebody} 的问候'.format(somebody=each_contact))
    print('-----------------------------------------------')

click_wechat_title_bar_back()

print('================================================================')
print('                           问候终了')
