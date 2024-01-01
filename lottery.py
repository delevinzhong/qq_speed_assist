from utils import *

if __name__ == '__main__':
    # 获取抽奖账号密码
    config_catalog = 'user_define'
    config_name = 'lottery_acc_pwd_dict'
    lottery_acc_pwd_dict = get_acc_pwd(config_catalog=config_catalog, config_name=config_name)
    # 登录账号密码并关闭弹窗
    login(acc_pwd_dict=lottery_acc_pwd_dict)
    # 移动到精灵世界
    move_to_elf_world()
    # 进入物品-功能页面
    move_to_items()
    # 开启第一个道具
    open_prop(1)
    # 等待12点继续开启道具
    wait_to(clicks=60)