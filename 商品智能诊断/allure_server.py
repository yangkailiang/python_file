
import os
import shutil

try:
    shutil.rmtree(r'/Users/ykl/商品智能诊断/report')
    print('删除成功')
except Exception as e:
    print(e)
    pass

# os.system('killall java')
os.system('python3 -m pytest /Users/ykl/商品智能诊断/test.py --alluredir report/allure_raw')
os.system('allure serve /Users/ykl/商品智能诊断/report/allure_raw')
