import datetime
import requests
import os
import sys
import yaml
from requests.packages import urllib3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Tools.tools import open_yml, get_path


class Write_token(object):
    def __init__(self, logger):
        self.__logger = logger
        self.__time = datetime.datetime.now()
        self.__config = open_yml(get_path('config'), self.__logger)

    def get_token(self):
        urllib3.disable_warnings()
        url = 0
        user = 0
        if self.__config['environment'] == 'prod':
            url = self.__config['prod_url']
            user = open_yml(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/Data/user/prod_user.yaml',
                            self.__logger)['user']
        elif self.__config['environment'] == 'test':
            url = self.__config['test_url']
            user = open_yml(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/Data/user/test_user.yaml',
                            self.__logger)['user']
        try:
            if len(user) <= 1:
                login_data = {'username': user[0][1], 'password': user[0][2]}
                login = requests.post(url, json=login_data, verify=False, timeout=5).json()
                self.__logger.logger.info('%s:登陆线上成功：%s' % (user[0][0], login['code']))
                return [login], [user[0][0]]
            else:
                res = []
                name = []
                for item in user:
                    login_data = {'username': item[1], 'password': item[2]}
                    login = requests.post(url, json=login_data, verify=False, timeout=5).json()
                    self.__logger.logger.info('%s:登陆线上成功：%s' % (item[0], login['code']))
                    res.append(login)
                    name.append(item[0])
                return res, name
        except Exception as e:
            self.__logger.logger.error('登陆失败，原因是：%s' % e)

    def write(self):
        try:
            old_time = open_yml(get_path('token'), self.__logger)['time']
        except Exception as e:
            old_time = datetime.datetime.now()
            self.__logger.logger.error('获取上次写入时间失败,原因是:%s' % e)
        try:
            if (self.__time - old_time).seconds >= self.__config['time_out'] * 60:
                res = self.get_token()
                with open(get_path('token'), 'w', encoding='utf-8') as f:
                    for item in range(len(res[1])):
                        now_token = {res[1][item]: {self.__config['token_key']: res[0][item]['data']['token']}}
                        yaml.dump(now_token, f)
                    time_now = {'time': self.__time}
                    yaml.dump(time_now, f)
                    self.__logger.logger.info('token写入成功')
            else:
                self.__logger.logger.info('token还在有效时间')
        except Exception as e:
            self.__logger.logger.error('token写入失败，原因是：%s' % e)


if __name__ == '__main__':
    from Tools.Generate_log import *
    token = Write_token(Logger())
    token.write()
