from utils import *
import pydirectinput as pdi
import logging

config_catalog = 'user_define'
config_name = 'acc_pwd_dict_3'
acc_pwd_dict = get_acc_pwd(config_catalog=config_catalog, config_name=config_name)
logging.basicConfig(filename='d://qq_speed_assist.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("--------------------------------------------------------------------------")

# 登录三个账号
login(acc_pwd_dict=acc_pwd_dict)

# 获取窗口名
qq_speed_title_list = get_qq_speed_window_list()
logging.info("QQ飞车窗口列表: {}".format(qq_speed_title_list))
acc_1_title = qq_speed_title_list[2]
acc_2_title = qq_speed_title_list[1]
acc_3_title = qq_speed_title_list[0]

# 账号1创建房间
logging.info("切换到账号1窗口")
activate_window(qq_speed_title_list[2])  # 切换至账号1
logging.info("创建房间")
create_dance_room()

# 账号1邀请账号2和账号3
account_list = []
for k in acc_pwd_dict.keys():
    account_list.append(k)
account_1 = account_list[0]
account_2 = account_list[1] # 获取账号2的QQ号码
account_3 = account_list[2] # 获取账号3的QQ号码
logging.info("邀请账号2 {}".format(account_2))
invite_account(account_2, acc_2_title, 2)
activate_window(acc_1_title)
sleep(2)
invite_account(account_3, acc_3_title, 3)
activate_window(acc_1_title)
sleep(1)

# 开始游戏
while True:
    img_start = './resources/start.png'
    logging.info("开始...")
    find_and_click(image_path=img_start, click_mode=1)  # 开始
    sleep(40)
    logging.info("账号1点击空格")
    pdi.click(x=1280, y=349)
    for i in range(1, 10):
        logging.info("按空格键")
        pdi.press('space')
        sleep(1)
    logging.info("账号2点击空格")
    activate_window(acc_2_title)
    sleep(1)
    pg.click(x=1280, y=349)
    for i in range(1, 10):
        logging.info("按空格键")
        pdi.press('space')
        sleep(1)
    logging.info("账号3点击空格")
    activate_window(acc_3_title)
    sleep(1)
    pg.click(x=1280, y=349)
    for i in range(1, 10):
        logging.info("按空格键")
        pdi.press('space')
        sleep(1)
    # 等待结束，截图，识别字体
    logging.info("等待结束")
    sleep(105)
    for title in qq_speed_title_list:   # 0: acc 2, 1: acc 1
        take_screen_shot(title)
        sleep(1)
    # send_screen_shot_to_wechat(account=account_1)
    # sleep(1)
    activate_window(acc_1_title)
    sleep(1)

