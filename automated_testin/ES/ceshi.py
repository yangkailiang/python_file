import logging

import csv

import datetime

from selenium import webdriver

data=datetime.datetime.now().strftime('%Y%m%d%H%M') #获取当前的时间

filename="timing_{}.csv".format(data) #创建一个csv文件

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

driver.maximize_window()

driver.find_element_by_id('kw').send_keys('性能测试')

driver.find_element_by_id('su').click()

#前端性能监控的接口

js = 'return window.performance.timing'

#执行JS脚本

timing = driver.execute_script(js)

print(timing)

logging.info(timing)

DNS_time=timing["domainLookupEnd"]-timing["domainLookupStart"] #DNS查询耗时

TCP_time = timing["connectEnd"] - timing["connectStart"] # TCP链接耗时

Requesr_time = timing["responseEnd"] - timing["responseStart"] # request请求耗时

dom_time = timing["domComplete"] - timing["domInteractive"] # 解析dom树耗时

# 白屏时间 白屏时间指的是浏览器开始显示内容的时间。因此我们只需要知道是浏览器开始显示内容的时间点，

# 即页面白屏结束时间点即可获取到页面的白屏时间。

white_screen= timing["responseStart"] - timing["navigationStart"]

domready_time = timing["domainLookupEnd"] - timing["domainLookupStart"] # DNS查询耗时

onload_time = timing["loadEventEnd"] - timing["navigationStart"] # onload时间

with open(filename, "a+", newline='') as csvfile:

    csv_write = csv.writer(csvfile)

# writerow 是一行一行写入 writerows方法是一次写入多行

    csv_write.writerow(["DNS查询耗时", "TCP链接耗时", "request请求耗时", "解析dom树耗时", "白屏时间", "DNS查询耗时", "onload时间"])

    csv_write.writerow([DNS_time, TCP_time, Requesr_time, dom_time,white_screen, domready_time, onload_time])

driver.quit()