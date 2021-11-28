import requests
from hot_diagnose.Tools.public_tools import login


class Api_data(object):
    def __init__(self, environment, shop_id, logger):
        self.logger = logger
        self.environment = environment
        self.shop_id = shop_id

    def environment(self):
        if self.environment == 'test':
            return 'http://saas-test.tmz1688.com/'
        elif self.environment == 'prod':
            return ''
        else:
            self.logger.logger.error('环境填错了')
            return None

    def get_msg_img(self):
        url = self.environment() + 'api/manage/user/gain/imgCode'
        res = requests.post(url)



    def get_commodity_data(self):


