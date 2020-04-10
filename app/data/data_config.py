# -*- coding:utf-8 -*-
class DataConfig:
    id = 0
    module = 1
    url = 2
    run = 3
    request_way = 4
    token = 5
    case_depend = 6
    data_depend = 7
    field_depend = 8
    data = 9
    expect = 10
    sql = 11
    result = 12

    # 获取caseid
    def get_id(self):
        return DataConfig.id

    # 获取模块
    def get_module(self):
        return DataConfig.module

    # 获取url
    def get_url(self):
        return DataConfig.url

    # 获取是否运行
    def get_run(self):
        return DataConfig.run

    # 获取请求类型
    def get_request_way(self):
        return DataConfig.request_way

    # 获取是否携带token
    def get_token(self):
        return DataConfig.token

    # 获取case依赖
    def get_case_depend(self):
        return DataConfig.case_depend

    # 获取依赖的返回数据
    def get_data_depend(self):
        return DataConfig.data_depend

    # 获取数据依赖字段
    def get_field_depend(self):
        return DataConfig.field_depend

    # 获取请求数据
    def get_data(self):
        return DataConfig.data

    # 获取预期结果
    def get_rexpect(self):
        return DataConfig.expect

    # 获取是否更新sql
    def get_sql(self):
        return DataConfig.sql

    # 获取实际结果
    def get_result(self):
        return DataConfig.result
