# -*- coding:utf-8 -*-
from app.util.operation_excel import OperationExcel
from app.data.data_config import DataConfig
from app.util.operation_json import OperationJson


class GetData():
    def __init__(self):
        self.data_config = DataConfig()
        self.opera_excel = OperationExcel()

    # 去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_run(self, rowx):
        flag = None
        colx = self.data_config.get_run()
        run = self.opera_excel.get_cell_value(rowx, colx)
        if run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取是否携带token
    def is_token(self, rowx):
        colx = self.data_config.get_token()
        token = self.opera_excel.get_cell_value(rowx, colx)
        if token == 'yes':
            return self.data_config.get_token_value()
        else:
            return None

    # 获取请求方式
    def get_request_way(self, rowx):
        colx = self.data_config.get_request_way()
        request_way = self.opera_excel.get_cell_value(rowx, colx)
        return request_way

    # 获取uil
    def get_url(self, rowx):
        colx = self.data_config.get_url()
        url = self.opera_excel.get_cell_value(rowx, colx)
        return url

    # 获取请求数据
    def get_data(self, rowx):
        colx = self.data_config.get_data()
        data = self.opera_excel.get_cell_value(rowx, colx)
        if data == '':
            return None
        return data

    # 通过获取关键词拿到data数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_data(row))
        return request_data

    # 获取预期结果
    def get_rexpect(self, rowx):
        colx = self.data_config.get_rexpect()
        rexpect = self.opera_excel.get_cell_value(rowx, colx)
        if rexpect == '':
            return None
        return rexpect

    # 获取sql数据
    def get_sql(self, rowx):
        colx = self.data_config.get_sql()
        sql = self.opera_excel.get_cell_value(rowx, colx)
        return sql


if __name__ == '__main__':
    data = GetData()
    print(data.get_url(1))
