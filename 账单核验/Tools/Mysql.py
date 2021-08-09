import pymysql
from sshtunnel import SSHTunnelForwarder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../")))

from Tools.tools import *
from Tools.Generate_log import *


class Mysql():
    def __init__(self, mysql_name):
        self.log = Logger()
        self.config = open_yml(get_path('config'), self.log)
        if self.config['environment'] == 'test':
            try:
                self.tunnel = SSHTunnelForwarder(
                                ('121.41.16.183', 22),  # 指定ssh登录的跳转机的address，端口号
                                ssh_username="root",  # 跳转机的用户
                                ssh_pkey=self.config['test_key_path'],  # 私钥路径
                                ssh_private_key_password="KI2w92iz",  # 密码（电脑开机密码）
                                remote_bind_address=('localhost', 3306))
                self.tunnel.start()
                self.conn = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                                            port=self.tunnel.local_bind_port,
                                            user='webapp',  # 数据库用户名
                                            passwd='KI2w92iz',  # 数据库密码
                                            db=mysql_name,
                                            charset='utf8',
                                            cursorclass=pymysql.cursors.DictCursor)
                self.cursor = self.conn.cursor()
                self.log.logger.info('连接test数据库成功:%s'%self.cursor)
            except Exception as e:
                self.log.logger.error('连接test数据库失败，原因是：%s'%e)
        elif self.config['environment'] == 'prod':
            try:
                self.tunnel = SSHTunnelForwarder(
                    ('39.101.219.110', 22),  # 指定ssh登录的跳转机的address，端口号
                    ssh_username="yangkailiang",  # 跳转机的用户
                    ssh_pkey=self.config['prod_key_path'],  # 私钥路径
                    ssh_private_key_password="LIfeEf3kL",  # 密码（电脑开机密码）
                    remote_bind_address=('rm-k2j4wjg5pl3z7h1f5.mysql.zhangbei.rds.aliyuncs.com', 3306))
                self.tunnel.start()
                self.conn = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                                            port=self.tunnel.local_bind_port,
                                            user='kuaimen_super',  # 数据库用户名
                                            passwd='super123!@#',  # 数据库密码
                                            db=mysql_name,
                                            charset='utf8',
                                            cursorclass=pymysql.cursors.DictCursor)  # 数据库名称
                self.cursor = self.conn.cursor()
                self.log.logger.info('连接prod数据库成功:%s' % self.cursor)
            except Exception as e:
                self.log.logger.error('连接prod数据库失败，原因是：%s' % e)

    def select_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            data = self.cursor.fetchall()
            self.log.logger.info('执行sql成功:%s'%sql)
            return data
        except Exception as e:
            self.log.logger.error('执行sql失败，原因是：%s'%e)


    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
            self.tunnel.close()
            self.log.logger.info('关闭游标、数据库连接、ssh连接成功')
        except Exception as e:
            self.log.logger.error('关闭游标、数据库连接、ssh连接失败,原因是：%s'%e)



if __name__ == '__main__':

    ssh = Mysql('kuaimen')

    print(ssh.select_sql("select * from team where id =1"))
    ssh.close()


