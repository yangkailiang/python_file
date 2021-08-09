import os
import requests
import sys
import urllib3
import yaml
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../")))


def open_yml(path, log):
    '''
    打开指定的yaml文件
    :param path: 路径（最好是绝对路径）
    :return: 改文件的所有数据，字典形式返回
    '''
    try:
        with open(path,'r',encoding='utf-8') as f:
            log.logger.info('打开%s成功'%path)
            return yaml.safe_load(f)
    except Exception as e:
        log.logger.error('打开%s失败,原因是：%s'%(path, e))


def write_yml(path, text):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(text, f)

    except Exception as e:
        return e



def get_path(which):
    if which == 'config':
        return os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Configuration_file/config.yaml'
    elif which == 'token':
        return os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Data/token.yaml'
    elif which == 'prod_url':
        return os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Data/prod_url.yaml'
    elif which == 'test_url':
        return os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Data/test_url.yaml'
    else:
        return '未找到该path'


def write_token():
    from Tools.Generate_log import Logger
    config = open_yml(get_path('config'), Logger())
    if config['environment'] == 'prod':
        url_login = 'https://saas.tmz1688.com/api/manage/user/login'
        login_data = {'Host': '121.41.16.183 saas.tmz1688.com', 'username': "17633641290", 'password': "wWr1KC7964"}
        urllib3.disable_warnings()
        login = requests.post(url_login, json = login_data, verify = False)
        token = login.json()['data']
        print(token)
        write_yml(get_path('token'), token)






if __name__ == '__main__':

    # write_yml('/Users/ykl/test_saas/Data/token.yaml')
    # path = open_yml(get_path('log'))
    # print(path)
    write_token()