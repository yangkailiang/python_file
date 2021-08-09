import pytest
import pytest_check
import allure
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Tools.Dingding import Dingding
from Api.user_system_api import User_system_api
from Tools.tools import *
from Tools.Generate_log import Logger
from Mysql.user_system_sql import *

# 初始化日志器对象
logger = Logger()
api = User_system_api(logger)
test_data = get_test_data('/Data/user_system/test_data/test_commercial.yaml', logger)
print(test_data)
# 注册的账号登陆时的token
my_token = 0
# 注册账号的手机号
my_phone = 0
# 注册账号时关联的销售人员的ID
my_sale_id = 0
# 注册账号时关联的销售人员的名字
my_sale_name = 0
# 注册账号时的企业负责人
my_contactName = 0
# 注册时的企业名称
my_name = 0


@allure.feature('saas基础版接口')
class Test(object):
    @pytest.mark.run(order=1)
    @allure.story('我是前置操作，保证测试应用状态为开')
    @allure.description('')
    def test_modify_state(self):
        pass

    @pytest.mark.run(order=2)
    @allure.story('邀请入驻接口：/manage/user/register/by/invitation')
    @allure.description('')
    @allure.step('正反案例，销售人员名字，企业名，企业负责人、电话')
    @pytest.mark.parametrize('case,sale_name,name,contactName,phone', test_data['test_invitation'][0], ids=test_data['test_invitation'][1])
    def test_invitation(self, case, sale_name, name, contactName, phone):
        global my_phone
        global my_sale_id
        global my_sale_name
        global my_contactName
        global my_name
        my_phone = phone
        sale_id = get_salesman_id(sale_name, logger)
        my_sale_id = sale_id
        my_sale_name = sale_name
        my_contactName = contactName
        my_name = name
        res = api.invitation(sale_id, name, contactName, phone)
        if case == 'true':
            pytest_check.equal(res['code'], 10000, print(res))
        elif case == 'false':
            pytest_check.equal(res['code'], 20000, print(res))

    @pytest.mark.run(order=3)
    @allure.story('获取短信验证码 ：/manage/user/send/smsCode')
    @allure.description('')
    @allure.step('正反案例，手机号')
    @pytest.mark.parametrize('case, phone', test_data['test_get_message'][0], ids=test_data['test_get_message'][1])
    def test_get_message(self, case, phone):

        # res = api.get_message(phone)
        if case == '正案例':
            pass
        elif case == '反案例':
            pass

    @pytest.mark.run(order=4)
    @allure.story('获取图形验证码 ：/manage/user/gain/imgCode')
    @allure.description('')
    @allure.step('正反案例，手机号')
    @pytest.mark.parametrize('case, phone', test_data['test_get_imgcode'][0], ids=test_data['test_get_imgcode'][1])
    def test_get_imgcode(self, case, phone):
        # res = api.get_imgcode(phone)
        if case == '正案例':
            pass
        elif case == '反案例':
            pass

    @pytest.mark.run(order=5)
    @allure.story('登陆-基础版 ：/manage/user/login')
    @allure.description('')
    @allure.step('正反案例，登陆手机号， 短信验证码， 图形验证码')
    @pytest.mark.parametrize('case, phone', test_data['test_login'][0], ids=test_data['test_login'][1])
    def test_login(self, case, phone):
        res = api.login(phone)
        if case == '正案例':
            if pytest_check.equal(res['code'], 10000):
                global my_token
                my_token = {'authorization': res['data']['token']}
        elif case == '反案例':
            pass

    @pytest.mark.run(order=6)
    @allure.story('企业基本信息接口：/manage/company/info')
    @allure.description('')
    @allure.step('正反案例 店铺ID')
    @pytest.mark.parametrize('case, shop_id', test_data['test_get_company'][0], ids=test_data['test_get_company'][1])
    def test_get_company(self, case, shop_id):
        # res = api.get_company(my_token, shop_id)
        if case == '正案例':
            pass
        elif case == '反案例':
            pass

    @pytest.mark.run(order=7)
    @allure.story('获取应用列表（验证应用是否开通）：/company/app/list')
    @allure.description('')
    def test_get_app_list(self):
        # res = api.get_app_list(my_token)
        pass

    @pytest.mark.run(order=8)
    @allure.story('我的订单列表：/manage/my/order/pageList')
    @allure.description('')
    def test_my_order_list(self):
        # res = api.my_order_list(my_token)
        pass

    @allure.story('购买-应用列表（获取报价）：/manage/app/goods/list')
    @allure.description('')
    @allure.step('正反案例, 应用ID， 版本：normal基础版')
    @pytest.mark.parametrize('case, app_id, edition', test_data['test_app_price_list'][0], ids=test_data['test_app_price_list'][1])
    def test_app_price_list(self, case, app_id, edition):
        # res = api.app_price_list(my_token, app_id, edition)
        if case == '正案例':
            pass
        elif case == '反案例':
            pass

    @allure.story('获取应用列表,判断登陆账号是否可以试用：/manage/app/getAllList')
    @allure.description('')
    def test_get_on_trial(self):
        # res = api.get_on_trial(my_token)
        pass
    @allure.story('试用-基础版：/manage/app/try')
    @allure.description('')
    @allure.step('正反案例, 应用ID， 版本：normal基础版')
    @pytest.mark.parametrize('case, app_id, edition', test_data['test_on_trial'][0], ids=test_data['test_on_trial'][1])
    def test_on_trial(self, case, app_id, edition):
        # res = api.on_trial(my_token, app_id, edition)
        if case == '正案例':
            pass
        elif case == '反案例':
            pass

    @allure.story('获取应用有效期：/manage/app/expireTime')
    @allure.description('')
    @allure.step('正反案例, 应用ID')
    @pytest.mark.parametrize('case, app_id', test_data['test_app_end_time'][0], ids=test_data['test_app_end_time'][1])
    def test_app_end_time(self, case, app_id):
        # res = api.app_end_time(my_token, app_id)
        if case == '正案例':
            pass
        elif case == '反案例':
            pass

    @allure.story('下单：/manage/app/expireTime')
    @allure.description('')
    @allure.step('正反案例, 应用ID')
    @pytest.mark.parametrize('case, app_id', test_data['test_app_end_time'][0], ids=test_data['test_app_end_time'][1])
    def test_app_end_time(self, case, app_id):
        # res = api.app_end_time(my_token, app_id)
        if case == '正案例':
            pass
        elif case == '反案例':
            pass











    @pytest.mark.last
    @allure.story('请忽略，这是我清理脏数据')
    def test_down(self):
        from conftest import dic
        passed = []
        failed = []
        error = []
        for name, result in enumerate(dic.items()):
            if result[1] == 'passed':
                passed.append(result)
            elif result[1] == 'failed':
                failed.append(result)
            else:
                error.append(result)
        Dingding(logger).send_dingding_msg('测试结果', '通过%d个，失败%d个，报错%d个，\n%s' % (len(passed), len(failed), len(error), (failed + error)))
        assert 1 == 2


