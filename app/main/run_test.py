# -*- coding:utf-8 -*-

from app.base.runmethod import RunMethod
from app.data.get_data import GetData
import unittest


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    # 程序执行的主入口
    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(2, rows_count):
            url = self.data.get_url(i)
            data = self.data.get_data_for_json(i)
            request_way = self.data.get_request_way(i)
            run = self.data.get_run(i)
            token = self.data.is_token(i)
            if run:
                res = self.run_method.run_main(request_way, url, data, token)
            return res


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
