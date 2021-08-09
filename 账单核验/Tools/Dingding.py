import sys
import hmac
import hashlib
import base64
import urllib.parse
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../")))
from Tools.Generate_log import *


def send_msg(title, send_text):
    logg = Logger()

    try:
        config = open_yml(get_path('config'), logg)
        timestamp = str(round(time.time() * 1000))
        secret = config['dingding_key']
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = config['dingding_url']
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
        r = requests.post(url,json=data,headers=headers)
        logg.logger.info('叮叮响应：%s' % r.json())
        return r.text
    except Exception as e:
        logg.logger.error('叮叮发送失败，原因是：%s' % e)




if __name__ == '__main__':
    import time

    data = send_msg('ceshi', 'aaaaa')
    time.sleep(2)
