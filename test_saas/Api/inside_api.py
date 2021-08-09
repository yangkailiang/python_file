import yaml
import requests
import os
import sys
from requests.packages import urllib3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Inside_api(object):
    def __init__(self, logger):
        from Tools.tools import get_url
        self.__logger = logger
        self.__url = get_url(self.__logger, 'user_system', 'mock')

    # post基类
    def post(self, name, data=None, header=None):
        try:
            urllib3.disable_warnings()
            res = requests.post(self.__url[name], json=data, headers=header, verify=False).json()
            self.__logger.logger.info('接口%s请求成功,返回为：%s' % (name, res))
            return res
        except Exception as e:
            self.__logger.logger.error('接口%s请求失败，原因是：%s' % (name, e))

    # 登陆-短信验证码&图形验证码
    def login(self, user=None, pwd=None, phone=None, msgcode=None, imgcode=None):
        data = {
            'username': user,
            'password': pwd,
            'phone': phone,
            'smsVerificationCode': msgcode,
            'imgVerificationCode': imgcode
        }
        return self.post('login', data)

    # 客户管理列表
    def user_list(self, tab=None, appVersion=None, common=None, pageSize=None):
        data = {
            'tab': tab,
            'appVersion': appVersion,
            'common': common,
            'pageSize': pageSize
                }
        return self.post('user_list', data)

    # 客户邀请列表
    def user_invitation_list(self, tab=None, common=None, pageSize=None):
        data = {
            'tab': tab,
            'common': common,
            'current': 1,
            'pageSize': pageSize
        }
        return self.post('user_invitation_list', data)

    # 获取账号列表
    def account_list(self):
        return self.post('account_list')

    # 客户订单管理
    def user_order(self, token, size, appid, phone):
        data = {
          'pageSize': size,
          'current': 1,
          'appId': appid,
          'phone': phone
        }
        return self.post('user_order', data, header=token)

    # 商品应用列表
    def all_app_list(self, token):
        return self.post('all_app_list', header=token)




if __name__ == '__main__':
    from Tools.Generate_log import *
    api = Inside_api(Logger())
    # print(api.user_list())
    # print(api.user_invitation_list())
    # print(api.account_list())
    # print(api.user_order({'token': 'aa'}, 1, 2, 222))
    print(api.all_app_list({'token': '11'}))