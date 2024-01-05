import configparser
import datetime
import getpass
import json
import os
import time
import concurrent.futures
import subprocess
import logging

import pyautogui as pg
import pydirectinput as pdi
import pygetwindow as gw

from time import sleep

import pythoncom
import pytz as pytz
import win32com.client
import win32con
import win32gui
from PIL import ImageGrab, Image

logging.basicConfig(filename='d://qq_speed_assist.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# pip install opencv-python -i https://pypi.mirrors.ustc.edu.cn/simple

def today_tmr():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    logging.info("昨天是 : {}".format(yesterday))
    logging.info("今天是 : {}".format(today))
    logging.info("明天是 : {}".format(tomorrow))
    return yesterday, today, tomorrow


def get_acc_pwd(config_catalog, config_name):
    # 获取配置文件信息中的账号密码
    config = configparser.ConfigParser()
    config.read('./resources/config', encoding='utf-8') # 读取配置文件
    acc_pwd_dict = config.get(config_catalog, config_name)
    config_dict = json.loads(acc_pwd_dict)  # 将字符串转为字典'
    result_dict = {}
    for k, v in config_dict.items():
        result_dict.update({k: v})
    return  result_dict


def login(acc_pwd_dict):
    for acc, pwd in acc_pwd_dict.items():
        logging.info("登录账号 {}...".format(acc))
        # 根据图片找到飞车启动程序并双击
        img_launcher = './resources/launcher.png'
        find_and_click(img_launcher, click_mode=2)
        sleep(2)
        # 设置分辨率
        logging.info("设置分辨率为1280*800*32")
        pg.click(x=1486, y=944, duration=1)
        pg.click(x=1490, y=1071, duration=1, clicks=5)
        pg.click(x=1403, y=1042, duration=1)
        # 去指定位置输入账号密码并回车
        logging.info("输入账号密码登录")
        pg.click(1497, 680, duration=1)
        pg.typewrite(acc)
        pg.click(1448, 712, duration=1)
        pg.typewrite(pwd)
        pg.press('enter')
        # login_verify()
        logging.info("等待30秒进入游戏界面")
        sleep(30)
        pg.click(x=1273, y=333, duration=1)
        logging.info("关闭弹窗")
        pg.press(keys='ESC', presses=5, interval=0.5)


def login_verify():
    sleep(5)
    find_and_click(image_path='./resources/verify_1.png', click_mode=1)
    sleep(1)
    find_and_click(image_path='./resources/verify_2.png', click_mode=1)
    sleep(1)
    find_and_click(image_path='./resources/verify_3.png', click_mode=1)
    sleep(1)
    find_and_click(image_path='./resources/verify_4.png', click_mode=1)
    sleep(1)
    find_and_click(image_path='./resources/verify_5.png', click_mode=1)
    sleep(1)
    find_and_click(image_path='./resources/verify_6.png', click_mode=1)
    sleep(1)
    find_and_click(image_path='./resources/verify_7.png', click_mode=1)
    sleep(1)
    find_and_click(image_path='./resources/verify_8.png', click_mode=1)
    sleep(1)
    find_and_click(image_path='./resources/verify_confirm.png', click_mode=1)


def find_and_click(image_path, click_mode, clicks=1, confidence=0.8):
    # 获取屏幕截图
    screenshot = ImageGrab.grab()
    # 读取目标图片
    target_image = Image.open(image_path)
    # 在屏幕截图中查找目标图片的位置
    try:
        # print("confidence = " + str(confidence))
        location = pg.locate(target_image, screenshot, confidence=confidence)
        if location:
            # 计算目标图片的中心坐标
            x, y = pg.center(location)
            # 模拟点击目标图片的中心位置
            # print(x, y)
            if click_mode == 1:
                pg.click(x, y, clicks=clicks, interval=0.01)
            elif click_mode == 2:
                pg.doubleClick(x, y)
            return True
        else:
            return False
    except pg.ImageNotFoundException:
        logging.info("未找到图片位置 - {}".format(image_path))


def go_to_qq_speed_title():
    title_list = pg.getAllTitles()
    qq_speed_title_list = []
    for title in title_list:
        if title.__contains__("QQ飞车"):
            qq_speed_title_list.append(title)
            window = gw.getWindowsWithTitle(title)
            # 检查是否找到窗口
            if window:
                # pg.FAILSAFE = False
                window = window[0]  # 如果有多个窗口，选择第一个
                logging.info("找到窗口: {title}")
                # 获取窗口位置
                x, y, width, height = window.left, window.top, window.width, window.height
                # 移动鼠标到窗口中心
                # pg.moveTo(x + width // 2, y + height // 2)
                # 移动鼠标到窗口顶部中心
                pg.moveTo(x + width // 2, y + 10)
                # 模拟鼠标点击
                pg.click()
                # 等待一段时间，确保窗口有足够时间响应
                time.sleep(2)
            else:
                logging.info("未找到窗口: {title}")
    return qq_speed_title_list


def set_resolution(mode=2):
    # 默认设置分辨率为1280 * 800
    # mode_dict = {0: "640 * 480", 1: "800 * 600", 2: "1024 * 768", 3: "960 * 600", 4: "1280 * 800", 5: "全屏"}
    logging.info("设置分辨率，默认设置为1280*800")
    if mode == 2:
        img_settings = './resources/settings.png'
        img_confirm = './resources/confirm.png'
        find_and_click(img_settings, 1, confidence=0.7)
        pg.click(x=1337, y=568, duration=0.5)
        pg.click(x=1337, y=653, duration=0.5)
        find_and_click(img_confirm, 1)


def create_dance_room():
    img_multiplayer_game = './resources/multiplayer_game.png'
    img_create_room = './resources/create_room.png'
    img_init_pattern = './resources/init_pattern.png'
    img_dance_mode = './resources/dance_mode.png'
    img_dance_traditional_pattern = './resources/dance_traditional_pattern.png'
    img_traditional_room = './resources/traditional_room.png'
    img_password = './resources/password.png'
    img_confirm = './resources/confirm.png'
    img_select_song = './resources/select_song.png'
    img_song = './resources/shuohaodexingfune.png'
    # img_start = './resources/start.png'

    find_and_click(image_path=img_multiplayer_game, click_mode=1)
    sleep(1)
    find_and_click(image_path=img_create_room, click_mode=1, confidence=0.6)
    sleep(1)
    find_and_click(image_path=img_init_pattern, click_mode=1)
    sleep(1)
    find_and_click(image_path=img_dance_mode, click_mode=1)
    sleep(1)
    find_and_click(image_path=img_dance_traditional_pattern, click_mode=1)
    sleep(1)
    find_and_click(image_path=img_traditional_room, click_mode=1, confidence=0.99)
    sleep(1)
    find_and_click(image_path=img_password, click_mode=1, confidence=0.99)
    sleep(1)
    find_and_click(image_path=img_confirm, click_mode=1)
    sleep(2)
    find_and_click(image_path=img_select_song, click_mode=1, confidence=0.9)
    sleep(1)
    find_and_click(image_path=img_song, click_mode=1)
    sleep(1)
    find_and_click(image_path=img_confirm, click_mode=1)
    sleep(1)
    # find_and_click(image_path=img_start, click_mode=1)


def invite_account(account, title, mode):
    img_friends = './resources/friends.png'
    img_find_friends = './resources/find_friends.png'
    img_confirm = './resources/confirm.png'
    img_invite = './resources/invite_to_join.png'

    if mode == 2:
        find_and_click(image_path=img_friends, click_mode=1) # 点击好友图标
        sleep(2)
    find_and_click(image_path=img_find_friends, click_mode=1) # 点击查找车手
    sleep(2)
    pg.typewrite(account) # 输入要查找的QQ号
    sleep(2)
    find_and_click(image_path=img_confirm, click_mode=1) # 确定
    sleep(3)
    # find_and_click(image_path=img_invite, click_mode=1) # 点击邀请
    pdi.click(x=909, y=951)
    sleep(2)
    pg.press('ESC') # 返回房间界面
    sleep(2)
    activate_window(title)   # 切换至账号2
    sleep(2)
    pg.click(x=1826, y=1066) # 接受邀请
    sleep(2)
    find_and_click(image_path=img_confirm, click_mode=1) # 确定
    sleep(2)
    pg.press('F5') # 准备
    sleep(2)


def move_to_elf_world():
    img_leisure = './resources/leisure.png'
    img_elf_world = './resources/elf_world.png'
    logging.info("打开休闲目录")
    find_and_click(image_path=img_leisure, click_mode=1)
    logging.info("进入精灵界面")
    find_and_click(image_path=img_elf_world, click_mode=1)
    sleep(1)


def move_to_items():
    img_items = './resources/items.png'
    logging.info("进入物品界面")
    find_and_click(image_path=img_items, click_mode=1)
    sleep(1)
    logging.info("进入功能界面")
    pg.click(x=821, y=539, duration=1)
    sleep(1)


def open_prop(order):
    if order == 1:
        logging.info("开启第 {} 个道具".format(order))
        pg.click(x=718, y=789, duration=1)
        pg.PAUSE = 1.0
        pg.click(x=1219, y=847, duration=1)


def continue_prop(clicks):
    img = './resources/continue.png'
    logging.info("继续抽奖，点击{}次".format(clicks))
    find_and_click(image_path=img, click_mode=1, clicks=clicks)
    # pg.click(x=1334, y=887, clicks=clicks)


def wait_to(clicks):
    flag = 1
    yesterday, today, tomorrow = today_tmr()
    logging.info("等待时间到凌晨12点...".format())
    while flag == 1:
        sh_tz = pytz.timezone('Asia/Shanghai')
        now = datetime.datetime.now(sh_tz).strftime('%Y-%m-%d %H:%M:%S')
        print(now)
        datetime_str = '{} 00:00:00'.format(tomorrow)
        if now >= datetime_str:
            continue_prop(clicks)
            logging.info("抽奖结束")
            flag = 2


def sync_timezone():
    logging.info("同步网络时间")
    pg.press('win')
    pg.PAUSE = 1.0
    pg.typewrite('timezone')
    pg.PAUSE = 1.0
    pg.press('enter')
    time.sleep(2)
    find_and_click(image_path='./resources/sync_tz.png', click_mode=1, clicks=20, confidence=0.9)


# 获取窗口句柄
# def get_window_handle(title):
#     handle = win32gui.FindWindow(None, title)
#     if handle <= 0:
#         raise Exception("窗口未找到！")
#         # handle = win32gui.FindWindow(None, title)
#     if handle > 0:
#         pythoncom.CoInitialize()
#         shell = win32com.client.Dispatch('WScript.Shell')
#         shell.SendKeys('%')
#     return handle


# 激活窗口
def activate_window(title):
    handle = win32gui.FindWindow(None, title)
    # if handle <= 0:
    #     raise Exception("找不到窗口{}".format(title))
    # else:
    #     print("激活窗口{}".format(title))
    #     shell = win32com.client.Dispatch("WScript.Shell")
    #     pg.press('ENTER')
    #     shell.SendKeys(' ')
    #     win32gui.SetForegroundWindow(handle)
    #     shell.SendKeys('%')
    if handle:
        win32gui.ShowWindow(handle, win32con.SW_RESTORE)
        win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)
        win32gui.SetForegroundWindow(handle)
    else:
        print("未找到窗口 ： {}".format(title))


def take_screen_shot(title):
    logging.info("切换到窗口 {} 并截图".format(title))
    activate_window(title)
    sleep(1)
    pg.press('F4')


def get_qq_speed_window_list():
    qq_speed_title_list = []
    title_list = pg.getAllTitles()
    for title in title_list:
        if title.__contains__("QQ飞车"):
            qq_speed_title_list.append(title)
    return qq_speed_title_list


def run_program(program):
    result = subprocess.run(
        ['python', program],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return program, result.returncode, result.stdout, result.stderr


def send_screen_shot_to_wechat(account):
    logging.info("发送账号{}的截图到微信".format(account))
    username = getpass.getuser()    # 获取windows系统用户名
    screen_shot_path = 'C:\\Users\\{}\\Documents\\QQ飞车\\{}\\截图'.format(username, account)
    logging.info("打开文件夹{}".format(screen_shot_path))
    os.startfile(screen_shot_path)
    sleep(1)
    logging.info("全选")
    pg.hotkey('ctrl', 'a')
    sleep(1)
    logging.info("复制")
    pg.hotkey('ctrl', 'c')
    sleep(1)
    logging.info("打开微信")
    activate_window('微信')
    sleep(1)
    img_wo = './resources/wo.png'
    find_and_click(image_path=img_wo, click_mode=1) # 找到wo的微信
    sleep(1)
    logging.info("粘贴")
    pg.hotkey('ctrl', 'v')
    sleep(1)
    logging.info("发送")
    pg.press('enter')
    sleep(1)
    logging.info("回到截图文件夹")
    os.startfile(screen_shot_path)
    logging.info("删除所有截图")
    pg.hotkey('ctrl', 'a')
    sleep(1)
    pg.hotkey('shift', 'delete')
    sleep(1)
    pg.press('enter')
    sleep(1)


# def run_double_mode():
#     program1 = "double_mode.py"
#     program2 = "take_screen_shot.py"
#
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # Concurrently execute the programs using threads
#         futures = [executor.submit(run_program, program) for program in [program1, program2]]
#
#         # Wait for all tasks to complete
#         concurrent.futures.wait(futures)
#
#         # Process results
#         for future in futures:
#             program, returncode, stdout, stderr = future.result()
#             print(f"{program} exited with return code {returncode}")
#             print(f"stdout:\n{stdout}")
#             print(f"stderr:\n{stderr}")
#             print("------")