# -*- coding:utf-8 -*-
import requests


class RunMethod:
    def post_main(self, url, data, token=None):
        res = None
        if token != None:
            res = requests.post(url=url, data=data, token=token).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def get_main(self, url, data, token=None):
        res = None
        if token != None:
            res = requests.get(url=url, params=data, token=token).json()
        else:
            res = requests.get(url=url, data=data).json()
        return res

    def run_main(self, url, method, data=None, token=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, token)
        else:
            res = self.get_main(url.data, token)
        return res

