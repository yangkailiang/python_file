import sys
import hmac
import hashlib
import base64
import urllib.parse
import os
import time
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Dingding(object):
    def __init__(self, logger):
        self.__logger = logger

    def send_dingding_msg(self, title, send_text):
        try:
            timestamp = str(round(time.time() * 1000))
            secret = 'SEC00431529b4caf06f954fcf1b30faf2ff763c75bcf540aa5bcf97853beaf24a14'
            secret_enc = secret.encode('utf-8')
            string_to_sign = '{}\n{}'.format(timestamp, secret)
            string_to_sign_enc = string_to_sign.encode('utf-8')
            hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
            sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
            url = 'https://oapi.dingtalk.com/robot/send?access_token=9ed3a8951e33b4708aacb790ad94fcab4cfcdffc42dd0721751cbb9745941f43'
            url = '{}&timestamp={}&sign={}'.format(url, timestamp, sign)
            headers = {'Content-Type': 'application/json;charset=utf-8'}
            text = '标题：%s\n%s\n'%(title, send_text)
            data = {
                "msgtype": "text",
                "text": {
                    "content":text
                        },
                "at": {
                    "isAtAll": True  # 此处为是否@所有人
                      }
                    }
            r = requests.post(url, json=data, headers=headers)
            self.__logger.logger.info('叮叮响应：%s' % r.json())
            return r.text
        except Exception as e:
            self.__logger.logger.error('叮叮发送失败，原因是：%s' % e)


if __name__ == '__main__':
    pass
