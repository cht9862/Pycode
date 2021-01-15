# coding=utf-8
import ttl_data

class Admin_Entrance:

    '''
    管理员鉴权信息模块
    自身self.ID同来辨别身份否正确
    '''

    def __init__(self):
        self.ID = 'y'

    # 验证管理员身份，并给出返回值
    def admin_checkout(self):
        admin_id = str(input('管理员登录* 验证身份ID >: ')).strip()
        if admin_id.lower() == self.ID:
            return True
        if admin_id.lower() != self.ID:
            return False

    # 接受验证函数的返回值，可以通过result 判断身份验证是否成功或失败
    def get_admin_check(self):
        result = self.admin_checkout()
        print(result)


class Adduser:
    '''
    管理会员和超市职员
    主要功能： 修改人员的相关信息
    '''

    def  __init__(self):
        pass

    def add_user(self, vla):
        self.adduser = ttl_data.UserVip(vla)
        self.adduser.set_user()

    def shop_staff(self):
        pass


class After_server:
    '''
    售后管理
    主要功能：退货、换货、退款等操作
    '''

    def __init__(self):
        pass

    def tui(self):
        pass

    def huan(self):
        pass

    def tui_money(self):
        pass


for i in range(100):
    a = {i: ['wo', 12, 123826485]}
    test = Adduser()
    test.add_user(a)