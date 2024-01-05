import pydirectinput as pdi
from utils import *

# img_confirm = './resources/confirm.png'
# img_gaizhuang = './resources/continue_gaizhuang.png'
# title_list = get_qq_speed_window_list()
# activate_window(title_list[0])
# sleep(1)
# for i in range(0, 8):
#     find_and_click(image_path=img_gaizhuang, click_mode=1, clicks=1)
#     find_and_click(image_path=img_confirm, click_mode=1, clicks=1)


pg.click(x=1273, y=333, duration=1)
img_get_daily_award = './resources/get_daily_award.png'
img_i_know = './resources/i_know.png'
img_close = './resources/close.png'
find_and_click(image_path=img_get_daily_award, click_mode=1)
sleep(2)
find_and_click(image_path=img_i_know, click_mode=1)
sleep(2)
find_and_click(image_path=img_close, click_mode=1)
sleep(1)
logging.info("关闭弹窗")
pg.press(keys='ESC', presses=5, interval=0.5)