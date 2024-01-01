import os

from utils import *

if __name__ == '__main__':
    print("请选择要运行的模式：\n1.单人刷道具（紫钻）\n2.双人刷道具\n3.抽奖")
    mode = input()
    if mode == "1":
        print("进入单人刷道具模式")
        os.system("python ./single_mode.py")
        exit(0)
    elif mode == "2":
        print("进入双人刷道具模式")
        os.system("python ./double_mode.py")
        exit(0)
    elif mode == "3":
        print("进入抽奖模式")
        sync_timezone()
        os.system("python ./lottery.py")
        exit(0)
    else:
        print("输入无法识别,程序结束")
        exit(1)