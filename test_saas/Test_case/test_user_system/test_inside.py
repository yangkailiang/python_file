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


@allure.feature('测试saas接口222')
class Test(object):
    logger = Logger()
    api = User_system_api(logger)
    test_data = get_test_data('/Data/user_system/test_data/test_inside.yaml', logger)

    @pytest.mark.parametrize('aa', [1,2,3,4])
    def test01(self, aa):
        global a
        if aa == 1:
            a = 10000000000

    def test02(self):
        pytest_check.is_not_none(None)

    # def test03(self):
    #     print(a)



