import os


import shutil
from Tools.Dingding import send_msg
def delet():
    try:
        shutil.rmtree(r'/Users/ykl/automated_testin/ES/report')
        print('删除成功')
    except Exception as e:
        print(e)
        pass
# delet()
os.system('killall java')
# os.system('python3 -m pytest /Users/ykl/automated_testin/ES/Test/test_bill.py -n auto --alluredir ./report/allure_raw')
# os.system('python3 -m pytest /Users/apple/python项目/automated_testin/ES/Test/test_bill.py -n auto --alluredir ./report/allure_raw')
os.system('nohup allure serve -p 8888 /Users/apple/python项目/automated_testin/ES/report/allure_raw &')
# 'allure generate F:\MyProject\My_First_allure\report -o F:\MyProject\My_First_allure\report\html --clean
# '
# http://192.168.10.48:3002/twoone/twoone
# send_msg('allure测试啦啦啦啦啦','http://192.168.40.147:8888/')



# pytest test_m1.py -m smoke -s
# 指定标签运行case
'''
windows
1、查看所有的端口
netstat -ano

2、查看指定端口
netstat -aon|findstr "9050"

3、查看指定PID的进程
tasklist|findstr "<指定PID>"

4、杀进程
taskkill /f /t /im 进程名

'''









