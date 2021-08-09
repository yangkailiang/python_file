import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Mail(object):
    def __init__(self, logger):
        self.__logger = logger

    def send_msg(self, receiver, mail_title, content):
        try:
            from Tools.tools import open_yml, get_path
            config = open_yml(get_path('config'), self.__logger)
            sender = config['sender']
            username = config['sender']
            password = config['password']
            if config['send_type'] == 'file':
                f = open(content, 'rb')
                mail_body = f.read()
                f.close()
                message = MIMEText(mail_body, 'html', 'utf-8')
                message['From'] = sender
                message['To'] = receiver
                message['Subject'] = Header(mail_title, 'utf-8')
            elif config['send_type'] == 'text':
                mail_body = content
                message = MIMEText(mail_body, 'text', 'utf-8')
                message['From'] = sender
                message['To'] = receiver
                message['Subject'] = Header(mail_title, 'utf-8')
            # 邮件内容, 格式, 编码
                smtp = smtplib.SMTP()
                smtp.connect('smtp.163.com')
                smtp.login(username, password)
                smtp.sendmail(sender, receiver, message.as_string())
                self.__logger.logger.info('发送邮件成功，接收者：%s'%receiver)
                smtp.quit()
        except Exception as e:
            self.__logger.logger.error("发送邮件失败！！！原因：%s"%e)


if __name__ == '__main__':
    from Generate_log import *
    mail = Mail(Logger())
    mail.send_msg('3171945535@qq.com', '测试主题', 'neirong')


