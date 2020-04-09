# -*- coding:utf-8 -*-
import json


# fp = open('E:/www/zhaoliangji/app/dataconfig/login.json')
# data = json.load(fp)
# print(data['login'])
class OperationJson:
    def __init__(self):
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open('D:/www/zhaoliangji/app/dataconfig/login.json') as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, id):
        return self.data[id]


if __name__ == '__main__':
    opjson = OperationJson()
    print (opjson.get_data('login'))
    print (opjson.get_data('favorite_list'))
