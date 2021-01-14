# coding='utf-8'

import json

class UserVip:

    '''
    存储vip 用户数据
    '''

    def __init__(self, name):
        self.name = name

    def get_key(self):
        # 遍历字典取key
        for i in self.name:
            return i

    def set_user(self):
        '''
        储存用户数据
        :return:
        '''
        filename = f'/Users/mac/PycharmProjects/函数编程学习/pro_name/data/{self.get_key()}.json'
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.name, file)
            print('用户数据储存成功。')

    def get_user(self):
        '''
        读取用户数据
        :return:
        '''
        filename = f'/Users/mac/PycharmProjects/函数编程学习/pro_name/data/{self.get_key()}.json'
        with open(filename, encoding='utf-8') as file:
            result = json.load(file)
            print(result)
            result1 = result[str(self.get_key())]
            print(f'vip 用户数据信息，姓名：{result1[0]} 年龄：{result1[1]} 电话号码：{result1[2]}')


s = {10011: ['李四', 23, 1399203823]}
test = UserVip(s)
test.get_user()

# print(s[10012])
