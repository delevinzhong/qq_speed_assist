from utils import *
import pyautogui as pg


def sleep(interval):
    for i in range(0, interval):
        print("等待{}秒".format(interval))
        interval -= 1
        time.sleep(1)


def sign_in():
    # 3.进入签到页面
    print("进入签到页面")
    find_and_click(image_path=img_sign_in, click_mode=1)
    find_and_click(image_path=img_sign_in_2, click_mode=1)
    sleep(4)
    # 4.点击签到
    print("点击签到")
    find_and_click(image_path=img_sign_in_now, click_mode=1)
    sleep(2)
    # 5.点击确认
    print("点击确认")
    find_and_click(image_path=img_sign_in_confirm, click_mode=1)
    sleep(1)
    # C:\Users\Delevin\Documents\leidian9\Pictures\Screenshots\
    # activate_window('小号')
    # sleep(1)
    pg.hotkey('ctrl', '0')
    # 6.返回
    print("返回")
    find_and_click(image_path=img_sign_in_back, click_mode=1)


def switch_account(acc_img):
    # 7.切换账号，点击菜单
    print("切换账号，点击菜单")
    find_and_click(image_path=img_sign_in_options, click_mode=1)
    find_and_click(image_path=img_sign_in_options_2, click_mode=1)
    sleep(1)
    # 8.找到并点击设置
    print("找到并点击设置")
    pg.moveTo(x=1240, y=748)
    sleep(1)
    pg.scroll(-400)
    sleep(1)
    find_and_click(img_sign_in_settings, 1)
    # find_and_click(img_sign_in_settings_2, 1)
    sleep(1)
    print("点击账号管理")
    # 9.点击账号管理
    find_and_click(img_sign_in_manage_account, 1)
    sleep(1)
    # 10.切换账号2
    print("切换账号2")
    find_and_click(acc_img, 1)
    sleep(1)
    # 11.返回到主页
    print("返回到主页")
    find_and_click(img_sign_in_back, 1)
    # find_and_click(img_sign_in_back_2, 1)
    sleep(1)
    find_and_click(img_sign_in_back, 1)
    # find_and_click(img_sign_in_back_2, 1)
    sleep(1)
    find_and_click(img_sign_in_options, 1)
    find_and_click(img_sign_in_options_2, 1)


def treasure_hunt(times):
    img_treasure_hunt = './resources/treasure_hunt.png'
    img_treasure_hunt_2 = './resources/treasure_hunt_2.png'
    img_five_stars = './resources/five_stars.png'
    img_best_today = './resources/best_today.png'
    img_quick_treasure = './resources/quick_treasure.png'
    img_treasure_confirm = './resources/treasure_confirm.png'
    find_and_click(image_path=img_treasure_hunt, click_mode=1)
    find_and_click(image_path=img_treasure_hunt_2, click_mode=1)
    sleep(4)
    find_and_click(image_path=img_five_stars, click_mode=1)
    sleep(2)
    find_and_click(image_path=img_best_today, click_mode=1)
    sleep(2)
    for i in range(0, times):
        print("第{}次寻宝".format(i+1))
        find_and_click(image_path=img_quick_treasure, click_mode=1)
        sleep(1)
        find_and_click(image_path=img_treasure_confirm, click_mode=1)
        sleep(15)
        find_and_click(image_path=img_treasure_confirm, click_mode=1)
        sleep(1)
    pg.hotkey('ctrl', '0')
    sleep(1)
    find_and_click(image_path=img_sign_in_back, click_mode=1)


if __name__ == '__main__':
    img_thunder = './resources/thunder.png'
    img_mobile_qq_speed = './resources/mobile_qq_speed.png'
    img_mine = './resources/mine.png'
    img_sign_in = './resources/sign_in.png'
    img_sign_in_2 = './resources/sign_in_2.png'
    img_sign_in_now = './resources/sign_in_now.png'
    img_sign_in_confirm = './resources/sign_in_confirm.png'
    img_sign_in_back = './resources/sign_in_back.png'
    img_sign_in_back_2 = './resources/sign_in_back_2.png'
    img_sign_in_options = './resources/sign_in_options.png'
    img_sign_in_options_2 = './resources/sign_in_options_2.png'
    img_sign_in_settings = './resources/sign_in_settings.png'
    img_sign_in_settings_2 = './resources/sign_in_settings_2.png'
    img_sign_in_manage_account = './resources/sign_in_manage_account.png'
    img_sign_in_avatar_1 = './resources/sign_in_avatar_1.png'
    img_sign_in_avatar_2 = './resources/sign_in_avatar_2.png'
    img_sign_in_avatar_3 = './resources/sign_in_avatar_3.png'
    img_sign_in_avatar_4 = './resources/sign_in_avatar_4.png'
    img_sign_in_login = './resources/sign_in_login.png'
    img_sign_in_qq_login = './resources/sign_in_qq_login.png'
    img_sign_in_qq_auth_login = './resources/sign_in_qq_auth_login.png'
    img_sign_input_pwd = './resources/sign_input_pwd.png'
    img_sign_in_qq_login_enter = './resources/sign_in_qq_login_enter.png'
    img_sign_in_qq_offlinen_confirm = './resources/sign_in_qq_offlinen_confirm.png'

    # 1.打开雷电模拟器
    print("1.打开雷电模拟器")
    find_and_click(image_path=img_thunder, click_mode=2)
    sleep(15)
    pdi.press('ESC', 5)
    # 2.打开掌上飞车
    print("2.打开掌上飞车")
    find_and_click(image_path=img_sign_in_qq_offlinen_confirm, click_mode=1)
    sleep(1)
    find_and_click(image_path=img_mobile_qq_speed, click_mode=1)
    sleep(10)
    find_and_click(image_path=img_sign_in_login, click_mode=1)
    sleep(2)
    find_and_click(image_path=img_sign_in_qq_login, click_mode=1)
    sleep(2)
    # find_and_click(image_path=img_sign_in_qq_auth_login, click_mode=1)
    # sleep(4)
    find_and_click(image_path=img_sign_input_pwd, click_mode=1)
    sleep(1)
    pdi.typewrite("18081005831")
    sleep(1)
    find_and_click(image_path=img_sign_in_qq_login_enter, click_mode=1)
    sleep(3)
    find_and_click(image_path=img_sign_in_qq_auth_login, click_mode=1)
    sleep(10)
    # 3.账号1签到
    print("3.账号1签到")
    sign_in()
    sleep(1)
    print("3.1.账号1寻宝")
    treasure_hunt(5)
    sleep(1)
    # 4.切换到账号2
    print("4.切换到账号2")
    switch_account(img_sign_in_avatar_2)
    sleep(1)
    # 5.账号2签到
    print("5.账号2签到")
    sign_in()
    sleep(1)
    # 6.切换到账号3
    print("6.切换到账号3")
    switch_account(img_sign_in_avatar_3)
    sleep(1)
    # 7.账号3签到
    print("7.账号3签到")
    sign_in()
    sleep(1)
    # 8.切换到账号4
    print("8.切换到账号4")
    switch_account(img_sign_in_avatar_4)
    sleep(1)
    # 9.账号4签到
    print("9.账号4签到")
    sign_in()
    sleep(1)
    # 10.切换回账号1
    print("8.切换回账号1")
    switch_account(img_sign_in_avatar_1)