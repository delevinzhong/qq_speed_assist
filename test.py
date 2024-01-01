from utils import *
import pydirectinput as pdi
import win32gui
import tkinter as tk

activate_window('微信')
sleep(1)
img_wo = './resources/weiba.png'
find_and_click(image_path=img_wo, click_mode=1)
