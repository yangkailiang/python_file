import os
import yaml
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def open_yml(path, log):
    '''
    打开指定的yaml文件
    :param path: 路径（最好是绝对路径）
    :return: 改文件的所有数据，字典形式返回
    '''
    try:
        with open(path,'r',encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        log.logger.error('打开%s失败,原因是：%s' % (path, e))


def get_path(which):
    if which == 'config':
        return os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/config.yaml'
    elif which == 'log_path':
        return os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Journal/sys.log'
    elif which == 'token':
        return os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Data/user/token.yaml'
    else:
        return '未找到该path'


def get_url(logger, project, environment=None):
    config = open_yml(get_path('config'), logger)
    if project == 'user_system':
        if environment == 'mock':
            return open_yml(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) +
                            '/Data/user_system/url/mock_url.yaml', logger)
        elif config['environment'] == 'prod':
            return open_yml(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) +
                            '/Data/user_system/url/prod_url.yaml', logger)
        elif config['environment'] == 'test':
            return open_yml(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) +
                            '/Data/user_system/url/test_url.yaml', logger)


def get_test_data(path, logger):
    try:
        test_data = open_yml(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + path, logger)
        for i in test_data:
            if len(test_data[i][0]) == len(test_data[i][1]):
                logger.logger.info('测试数据读取成功')
                return test_data
            else:
                logger.logger.error('测试数据读取失败，请检查：%s' % i)
                break
    except Exception as e:
        logger.logger.error('测试数据读取失败,原因是：%s' % e)




if __name__ == '__main__':
    from Tools.Generate_log import *
    # test_data = open_yml(get_path('test_data'), Logger())
    # for i in test_data:
    #     print(i)
    # write_yml('/Users/ykl/test_saas/Data/token.yaml')
    # path = open_yml(get_path('log'))
    # print(path)
    # write_token()
    # a = get_test_data('test_data', Logger())
    # print(a)
