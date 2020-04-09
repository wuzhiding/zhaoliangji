import requests
import json


class RunMain:

    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)

    def __init__(self):
        self.res = self

    def send_get(self, url, data):
        res = requests.get(url=url, params=data).json()
        #tmp = json.dumps(res, indent=2, sort_keys=True)
        return json.dumps(res, indent=2, sort_keys=True)

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    url = 'http://testuser.zhaoliangji.com/api/favorite/list'
    data = {
        'user_id': '2097211',
        'page': '1',
        'token': 'b9e74f9e47beccdbf5aaa9aabb8d83f7',
        'status': '1'
    }
    run = RunMain(url, 'GET', data)
    print (run.run_main(url,'GET',data))
