# -*- coding:utf-8 -*-
class global_var:
    id = '0'
    module='1'
    url = '2'
    run = '3'
    request_way = '4'
    token = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    sql='11'
    result = '12'
#获取caseid
    def get_id(self):
        return global_var.id

#获取模块
    def get_module(self):
        return global_var.module
#获取url
    def get_url(self):
        return global_var.url
#获取是否运行
    def get_run(self):
        return global_var.run
#获取请求类型
    def get_request_way(self):
        return global_var.request_way
#获取是否携带token
    def get_token(self):
        return global_var.token
#获取case依赖
    def get_case_depend(self):
        return global_var.case_depend
#获取依赖的返回数据
    def get_data_depend(self):
        return global_var.data_depend
#获取数据依赖字段
    def get_field_depend(self):
        return global_var.field_depend
#获取请求数据
    def get_data(self):
        return global_var.data
#获取预期结果
    def get_rexpect(self):
        return global_var.expect
#获取是否更新sql
    def get_sql(self):
        return global_var.sql
#获取实际结果
    def get_result(self):
        return global_var.result