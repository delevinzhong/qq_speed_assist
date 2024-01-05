#Get-Content d:\qq_speed_assist.log -Tail 10 -Wait
#Get-Content c:\qq_speed_award.txt -Tail 10 -Wait
#cd D:\QQ_Speed_Assist\qq_speed_assist\
#python main.py

from utils import *

# get logs cmd
#       Get-Content D:\qq_speed_assist.log -Tail 10 -Wait
# install opencv timeout issue
#       pip install opencv-python -i https://pypi.mirrors.ustc.edu.cn/simple
# Could not build wheels for opencv-python which use PEP 517 and cannot be installed directly
#       pip install --upgrade pip setuptools wheel
if __name__ == '__main__':
    print("请选择要运行的模式：\n1.单人刷道具（紫钻）\n2.双人刷道具\n3.抽奖\n4.掌飞签到\n5.三人刷道具")
    mode = input()
    if mode == "1":
        print("进入单人刷道具模式")
        # os.system("python ./single_mode.py")
        os.system("python C:\\Users\\Delevin\\PycharmProjects\\Python-Projects\\qq_speed_assist\\dance_mode_single.py")
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
    elif mode == "4":
        print("进入掌飞每日签到模式")
        os.system("python ./auto_sign_in.py")
    elif mode == "5":
        print("进入三人刷道具模式")
        os.system("python ./triple_mode.py")
        exit(0)
    else:
        print("输入无法识别,程序结束")
        exit(1)