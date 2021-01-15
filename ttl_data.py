# coding='utf-8'

import json, sys, os


class UserVip:

    '''
    存储vip 用户数据
    '''

    def __init__(self, name):
        self.name = name
        # 获取系统信息
        self.system = sys.platform
        self.dirname = 'user_vip\\'
        self.dirname1 = 'user_vip/'
        # 获取当前目录下的文件和目录存在列表中返回给sysdir
        sysdir = os.listdir()
        if 'win' in self.system.lower() and 'user_vip' not in sysdir: os.system('md user_vip')
        if 'linux' in self.system.lower() and 'user_vip' not in sysdir: os.system('mkdir user_vip')
        if 'win' in self.system.lower():
            self.basename = os.path.join(os.getcwd(), f"{self.dirname}")
        elif 'linux' in self.system.lower():
            self.basename = os.path.join(os.getcwd(), f"{self.dirname1}")
        # 拼接存放json文件的目录绝对路径


    def get_key(self):
        # 遍历字典取key,取用户id
        for i in self.name:
            return i

    def set_user(self):
        '''
        储存用户数据
        :return:
        '''

        filename = f'{self.basename}{self.get_key()}.json'
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.name, file)
            print('用户数据储存成功。')


    def get_user(self):
        '''
        读取用户数据
        :return:
        '''
        filename = f'{self.basename}{self.get_key()}.json'
        with open(filename, encoding='utf-8') as file:
            result = json.load(file)
            result1 = result[str(self.get_key())]
            print(f'VIP用户信息>> \n\t姓名：{result1[0]}\n\t年龄：{result1[1]}  \n\t电话号码：{result1[2]}')

    def del_vip(self):
        result = ''.join(input('输入将要删除用户编号:>>'))
        result1 = ''.join(result.lower()+'.json')
        if 'win' in self.system.lower(): os.system(f'del {self.basename}{result1}')
        if 'linux' in self.system.lower(): os.system(f'rm -rf {self.basename}{result1}')


class Staff:

    '''
    存储员工信息数据
    '''

    def __init__(self, name):
        self.name = name
        # 获取当前系统类型信息
        self.system = sys.platform
        self.dirname = 'staff\\'
        self.dirname1 = 'staff/'
        # 获取当前目录下的文件和目录存在列表中返回给sysdir
        sysdir = os.listdir()
        if 'win' in self.system.lower() and 'staff' not in sysdir: os.system('md staff')
        if 'linux' in self.system.lower() and 'staff' not in sysdir: os.system('mkdir staff')
        if 'win' in self.system.lower():
            self.basename = os.path.join(os.getcwd(), f"{self.dirname}")
        elif 'linux' in self.system.lower():
            self.basename = os.path.join(os.getcwd(), f"{self.dirname1}")
        self.bba = os.system('cd staff')

    def get_key(self):
        # 遍历字典取key,取用户id
        for i in self.name:
            return i

    def set_user(self):
        '''
        储存用户数据
        :return:
        '''

        filename = f'{self.basename}{self.get_key()}.json'
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.name, file)
            print('用户数据储存成功。')

    def get_user(self):
        '''
        读取用户数据
        :return:
        '''
        filename = f'{self.basename}{self.get_key()}.json'
        with open(filename, encoding='utf-8') as file:
            result = json.load(file)
            result1 = result[str(self.get_key())]
            print(f'员工数据信息>> \n\t姓名：{result1[0]}\n\t年龄：{result1[1]}  \n\t电话号码：{result1[2]}')

    def del_vip(self):
        result = ''.join(input('输入将要删除用户编号:>> '))
        result1 = ''.join(result.lower()+'.json')
        if 'win' in self.system.lower(): os.system(f'del {self.basename}{result1}')
        if 'linux' in self.system.lower(): os.system(f'rm -rf {self.basename}{result1}')




# a = {1002: ['your', 13, 15945646828]}
# test = UserVip(a)
# test.set_user()
# test.get_user()


