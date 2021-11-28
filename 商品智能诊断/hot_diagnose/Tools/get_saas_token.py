import requests
import yaml
import os
import base64


class Get_token(object):
    def __init__(self, logger, environment):
        self.environments = environment
        self.logger = logger
        self.key_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Data/img_msg_key.yaml'
        self.token_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Data/token.yaml'
        self.img_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Data/img.gif'

    def environment(self):
        if self.environments == 'test':
            return 'http://saas-test.tmz1688.com/'
        elif self.environments == 'prod':
            return ''
        else:
            self.logger.logger.error('环境填错了')
            return None

    def write_yaml(self, path, data):
        with open(path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f)

    def read(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    def get_msg_img(self):
        url = self.environment() + 'api/manage/user/gain/imgCode'
        res = requests.post(url).json()
        self.write_yaml(self.key_path, {'img_msg_key': res['data']['key']})
        img_data = base64.b64decode(res['data']['img'].split(',')[1])
        with open(self.img_path, "wb") as f:
            f.write(img_data)

    def login(self):


    def main(self):




if __name__ == '__main__':
    from hot_diagnose.Tools.Generate_log import Logger
    logger1 = Logger()
    obj = Get_token(logger=logger1, environment='test')
    obj.get_msg_img()