# -*- coding:utf-8 -*-
import unittest
from app.base.demo import RunMain
import demjson
import HTMLTestRunner
import mock
from ddt import ddt,data,unpack


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'https://testuser.zhaoliangji.com/api/login/index'
        data = {
            'username': '18923455929',
            'password': 'a123456',
            'x_group_id': '26',
            'x_utm': '27'
        }
        mock.Mock()
        res = demjson.decode(self.run.run_main(url, 'POST', data))
        self.assertNotEqual(res['code'], 1, "测试失败")
        # globals()['token'] = 'b9e74f9e47beccdbf5aaa9aabb8d83f7'

    # @unittest.skip('test_02')  # 跳过不执行
    def test_02(self):
        # print(token)
        url = 'http://testuser.zhaoliangji.com/api/favorite/list'
        data = {
            'user_id': '2097211',
            'page': '1',
            'token': 'b9e74f9e47beccdbf5aaa9aabb8d83f7',
            'status': '1'
        }
        res = demjson.decode(self.run.run_main(url, 'GET', data))
        self.assertNotEqual(res['code'], 1, "测试失败")


if __name__ == '__main__':
    # unittest.main()
    # filepath = "report.html"
    outfile = open("D:/www/zhaoliangji/app/report/report.html", "wb")
    # fp = file(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='测试报告', description='测试用例情况:')
    runner.run(suite)

    # unittest.TextTestRunner().run(suite)
