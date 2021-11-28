import pymysql
from sshtunnel import SSHTunnelForwarder
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Mysql(object):
    def __init__(self, environment, mysql_name, logger):
        self.__logger = logger
        if environment == 'test':
            try:
                self.tunnel = SSHTunnelForwarder(
                                ('121.41.16.183', 22),  # 指定ssh登录的跳转机的address，端口号
                                ssh_username="root",  # 跳转机的用户
                                ssh_pkey='/Users/apple/Documents/数据库密钥/开发环境超管.pem',  # 私钥路径
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
                self.__logger.logger.info('连接测试环境：%s 数据库成功' % mysql_name)
            except Exception as e:
                self.__logger.logger.error('连接测试环境：%s 数据库失败:%s' % (mysql_name, e))
        elif environment == 'prod':
            try:
                self.tunnel = SSHTunnelForwarder(
                    ('39.101.219.110', 22),  # 指定ssh登录的跳转机的address，端口号
                    ssh_username="yangkailiang",  # 跳转机的用户
                    ssh_pkey='/Users/apple/Documents/数据库密钥/yangkailiang',  # 私钥路径
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
                self.__logger.logger.info('连接线上：%s 数据库成功' % mysql_name)
            except Exception as e:
                self.__logger.logger.error('连接线上：%s 数据库失败，原因是：%s' % (mysql_name, e))

    def select_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            self.__logger.logger.error('执行sql失败，原因是：%s' % e)

    def delete(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.conn.rollback()
            self.__logger.logger.info('删除数据成功，sql：%s' % sql)
        except Exception as e:
            self.conn.rollback()
            self.__logger.logger.error('删除数据失败，原因是：%s，' % e)

    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
            self.tunnel.close()
            self.__logger.logger.info('关闭游标、数据库连接、ssh连接成功')
        except Exception as e:
            self.__logger.logger.error('关闭游标、数据库连接、ssh连接失败,原因是：%s'%e)



if __name__ == '__main__':
    pass
    # from Generate_log import *
    # ssh = Mysql('kuaimen', Logger())
    # ssh.delete('delete from team_member where id =596')
    # print(ssh.select_sql("select * from team_member where id =596"))
    # ssh.close()



