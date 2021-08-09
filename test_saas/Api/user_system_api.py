import yaml
import requests
import os
import sys
from requests.packages import urllib3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class User_system_api(object):
    def __init__(self, logger):
        from Tools.tools import get_url
        urllib3.disable_warnings()
        self.__logger = logger
        self.__url = get_url(self.__logger, 'user_system', 'mock')

    # post基类
    def post(self, name, content_type=None, data=None, header=None):
        try:
            if content_type is None:
                res = requests.post(self.__url[name], json=data, headers=header, verify=False).json()
                self.__logger.logger.info('接口%s请求成功,返回为：%s' % (name, res))
                return res
            elif content_type == 'data':
                res = requests.post(self.__url[name], data=data, headers=header, verify=False).json()
                self.__logger.logger.info('接口%s请求成功,返回为：%s' % (name, res))
                return res
        except Exception as e:
            self.__logger.logger.error('接口%s请求失败，原因是：%s' % (name, e))

    # get基类
    def get(self, name, content_type=None, data=None, header=None):
        try:
            if content_type is None:
                res = requests.get(self.__url[name], json=data, headers=header, verify=False).json()
                self.__logger.logger.info('接口%s请求成功,返回为：%s' % (name, res))
                return res
            elif content_type == 'data':
                res = requests.get(self.__url[name], data=data, headers=header, verify=False).json()
                self.__logger.logger.info('接口%s请求成功,返回为：%s' % (name, res))
                return res
        except Exception as e:
            self.__logger.logger.error('接口%s请求失败，原因是：%s' % (name, e))

    # 获取手机验证码
    def get_message(self, phone):
        data = {'phone': phone}
        return self.post('get_message', data)

    # 获取邀请链接
    def get_invitation_url(self):
        return self.post('get_invitation_url')

    # 邀请入驻
    def invitation(self, sale_id, name, contactName, phone):
        data = {
            'saleUserID': sale_id,
            'name': name,
            'contactName': contactName,
            'phone': phone
        }
        return self.post('invitation', content_type='data', data=data)

    # 获取销售人员信息
    def get_sale(self, invitation_url):
        data = {'u': invitation_url}
        return self.post('get_sale', data)

    # 获取企业信息
    def get_company(self, token, shop_id):
        data = {'shopId': shop_id}
        return self.post('get_company', data=data, header=token)

    # 获取用户的应用列表（查看应用是否开通）
    def get_app_list(self, token):
        return self.post('get_app_list', header=token)

    # 获取图片验证码
    def get_imgcode(self, phone):
        data = {'phone': phone}
        return self.post('get_imgcode', data)

    # 登陆-短信验证码&图形验证码
    def login(self, user=None, pwd=None, phone=None, msgcode=None, imgcode=None):
        data = {
           'username': user,
           'password': pwd,
           'phone': phone,
           'smsVerificationCode': msgcode,
           'imgVerificationCode': imgcode
        }
        print(data)
        return self.post('login', data=data)

    # 获取我的订单列表
    def my_order_list(self, token):
        data = {
            'pageSize': 50,
            'current': 1,
        }
        return self.post('my_order_list', data, header=token)

    # 获取可购买的应用报价列表
    def app_price_list(self, token, app_id, edition):
        data = {'appId': app_id,
                'typeName': edition}
        return self.post('app_price_list', data, header=token)

    # 获取商品到期时间
    def app_end_time(self, token, app_id):
        data = {'appId': app_id}
        return self.post('app_end_time',  data, header=token)

    # 基础班-购买-续费===》下单
    def app_do_order(self, token, app_id):
        data = {'id': app_id}
        return self.post('app_do_order', data, header=token)

    # 基础班-购买-续费====》支付
    def app_do_pay(self, token, app_id, price):
        data = {'id': app_id, 'actualAmount': price}
        return self.post('app_do_pay', data, header=token)

    # 获取应用列表-查看是否可以试用
    def get_on_trial(self, token):
        return self.post('get_on_trial', header=token)

    # 试用-基础版
    def on_trial(self, token, app_id, edition):
        data = {'id': app_id, 'typeName': edition}
        return self.post('on_trial', header=token, data=data)

    # 取消订单
    def cancel_order(self, token, order_id):
        data = {'id': order_id}
        return self.post('cancel_order', data=data, header=token)

    # 获取续费后的到期时间
    def get_expire_time(self, token, app_id):
        data = {'id': app_id}
        return self.post('get_expire_time', data=data, header=token)

    # 订单支付结果查询
    def app_do_pay_select(self, token, order_num):
        data = {'orderNo': order_num}
        return self.post('app_do_pay_select', data=data, header=token)

    # 用户反馈
    def user_feedback(self, token, content):
        data = {'content': content}
        self.post('user_feedback', data=data, header=token)

    # 用户反馈列表
    def user_feedback_list(self, token):
        self.get('user_feedback_list', header=token)

    # 用户反馈详情
    def user_feedback_details(self, token, feedback_id):
        data = {'id': feedback_id}
        self.post('user_feedback', data=data, header=token)

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
    from Tools.Generate_log import Logger
    from Tools.tools import open_yml, get_path, get_url
    log = Logger()
    api = User_system_api(log)
    token1 = {'aa': 'aa'}
    # api.login(17633641290, 'wWr1KC7964')
    # print(api.get_message(11))
    # print(api.get_invitation_url())
    # print(api.invitation(1, 'ykll', 'ykll', '111'))
    # print(api.get_sale('aaa'))
    # print(api.get_company(11))
    # print(api.get_app_list())
    # print(api.get_imgcode(1111))
    print(api.login(phone=1111, msgcode=1111))
    # print(api.my_order_list({'token': '11'}))
    # token = open_yml(get_path('token'), log)['ykl1']
    # print(type(token))
    # print(api.app_price_list(token, 11))
    # print(api.app_end_time({'token':'11'}, 11))
    # print(api.app_do_order({'token':'11'}, 11))
    # print(api.app_do_pay({'token':'11'}, 11, 12))
    # print(api.user_list())
    # print(api.user_invitation_list())
    # print(api.account_list())
    # print(api.user_order({'token': 'aa'}, 1, 2, 222))
    # print(api.all_app_list({'token': '11'}))
    # print(api.on_trial(token1, 1, 'normal'))
    # print(api.get_expire_time(token1, 1))
    # print(api.app_do_pay_select(token1, 111))
    # print(api.cancel_order(token1, 11))
