#coding = utf-8
#author=cqz

import requests

class TestToken:
    #设置代理127.0.0.1:8888
    proxies = {"https": "http://127.0.0.1:8888"}
    def setup(self):
        self.token = self.get_token()
    #获取access_token信息
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwbf5bbb0bc23e75c1&corpsecret=j9EAgkj73oWg2tZ-vdsJipfUdXIVWTAuCQIEMZU5rMI"
        r = requests.get(url, proxies=self.proxies, verify=False)
        # r = requests.get(url)
        # print(r.text)
        return r.json()['access_token']
    #新增成员
    def test_post_create(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "chenyi",
            "name": "陈一",
            "mobile": "+86 13800000001",
            "department": [1]
        }
        r = requests.post(url, json=data, verify=False)
        print(r.json())
        #通过返回的状态码断言
        assert r.json()['errcode'] == 0

    #删除成员
    def test_get_delete(self):
        userid = "chenyi"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        r = requests.get(url,verify=False)
        print(r.json())
        assert r.json()['errcode'] == 0

    #更新成员信息
    def test_post_update(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "chenyi",
            "name": "陈二",
            "mobile": "+86 13800000002",
            "department": [1]
        }
        r = requests.post(url, json=data, verify=False)
        print(r.json())
        assert r.json()['errcode'] == 0

    #获取成员信息
    def test_get_user(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        userid = "ChenQinZhao"
        r = requests.get(url, proxies=self.proxies, verify=False)
        print(r.json())
        assert r.json()['errcode'] == 0

