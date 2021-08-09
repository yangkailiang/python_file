import smtplib
from email.mime.text import MIMEText
from email.header import Header


sender = '17633641290@163.com'
receiver = '1287073500@qq.com'
smtpserver = 'smtp.163.com'
username = '17633641290@163.com'
password = 'JWBCCLNEDIYCHOPH'


# 邮件主题
mail_title = '主题：测试报告3'


# 读取html文件内容
f = open('E:\\test_mtx\\Log\\Report\\report.html', 'rb')
mail_body = f.read()
f.close()


# 邮件内容, 格式, 编码
message = MIMEText(mail_body, 'html', 'utf-8')
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(mail_title, 'utf-8')


try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, message.as_string())
    print("发送邮件成功！！！")
    smtp.quit()
except smtplib.SMTPException:
    print("发送邮件失败！！！")