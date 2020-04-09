# -*- coding:utf-8 -*-
from app.util.operation_excel import OperationExcel
from .import data_config
from app.util.operation_json import OperationJson


class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    # 去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_run(self, row):
        flag = None
        col = data_config.get_run()
        run = self.opera_excel.get_cell_value(row, col)
        if run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取是否携带token
    def is_token(self, row):
        col = data_config.get_token()
        token = self.opera_excel.get_cell_value(row, col)
        if token == 'yes':
            return data_config.get_token_value()
        else:
            return None

    # 获取请求方式
    def get_request_way(self, row):
        col = data_config.get_request_way()
        request_way = self.opera_excel.get_cell_value(row, col)
        return request_way

    # 获取uil
    def get_url(self, row):
        col = data_config.get_url()
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_dat(self, row):
        col = data_config.get_data()
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 通过获取关键词拿到data数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_dat(self.get_data(row))
        return request_data

    # 获取预期结果
    def get_rexpect(self,row):
        col = data_config.get_rexpect()
        rexpect = self.opera_excel.get_cell_value(row, col)
        if rexpect == '':
            return None
        return rexpect


