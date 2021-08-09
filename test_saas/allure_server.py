import os

import requests
from Tools.tools import *
from Tools.Generate_log import *
from Tools.Write_token import *
# os.system("lsof -i :8881 | grep -i LISTEN | awk '{print $2}' | xargs -I {} kill -15 {}")
#
# os.system('python3 -m pytest /Users/apple/python_file/test_saas/Test_case/test_inside.py -n auto --alluredir ./report')
# # os.system('allure generate /Users/apple/python_file/test_saas/report -o /Users/apple/python_file/test_saas/report/html --clean ')
# os.system('nohup allure serve -p 8881 /Users/apple/python_file/test_saas/report &')
# Write_token(Logger()).write()
url = 'https://saas.tmz1688.com/api/shop/list'
token = open_yml(get_path('token'), Logger())['ykl1']
data = {'current': 0, 'keyword': "", 'pageSize': 10}
# print(token)
res = requests.post(url, json=data, headers=token).json()
print(res)