import pymysql



from sshtunnel import SSHTunnelForwarder

class Mysql(object):
    #
    # def write_image_mysql(self,mysql_name,file_path):
    #     '''
    #     将指定照片以二进制的格式保存至数据库
    #     :param file_path: 要保存的图片的位置
    #     :return: 无返回
    #     '''
    #     conn = Mysql().connect_mysql(mysql_name)
    #     with open(file_path, 'rb') as f:
    #         img = f.read()
    #     cur = conn.cursor()
    #     sql = "INSERT INTO image VALUES  (null,%s)"
    #     cur.execute(sql, img)
    #     conn.commit()
    #     cur.close()
    #     conn.close()
    # def read_img_mysql(selfuser,mysql_name,sql,file_path):
    #     conn = Mysql().connect_mysql(mysql_name)
    #     cur = conn.cursor()
    #     cur.execute(sql)
    #     fout = open(file_path, 'wb')
    #     liat = list(cur.fetchone())
    #     print(liat)
    #     fout.write(liat[0])
    #     fout.close()
    #     cur.close()
    #     conn.close()
    # def select_mysql(self,mysql_name,sql):
    #
    #     with SSHTunnelForwarder(
    #             ('121.41.16.183', 22),  # 指定ssh登录的跳转机的address，端口号
    #             ssh_username="root",  # 跳转机的用户
    #             ssh_pkey="/Users/ykl/Documents/开发环境超管.pem",  # 私钥路径
    #             ssh_private_key_password="KI2w92iz",  # 密码（电脑开机密码）
    #             remote_bind_address=('localhost', 3306)) as server:  # mysql服务器的address，端口号
    #         conn = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
    #                                port=server.local_bind_port,
    #                                user='webapp',  # 数据库用户名
    #                                passwd='KI2w92iz',  # 数据库密码
    #                                db=mysql_name,
    #                                charset='utf8',
    #                                cursorclass=pymysql.cursors.DictCursor)  # 数据库名称
    #         cur = conn.cursor()
    #         cur.execute(sql)
    #         data = cur.fetchall()
    #         cur.close()
    #         return data

    def select_mysql(self,mysql_name,sql):
        with SSHTunnelForwarder(
                # server.local_bind_port
                ('39.101.219.110', 22),  # 指定ssh登录的跳转机的address，端口号
                ssh_username="yangkailiang",  # 跳转机的用户
                ssh_pkey="/Users/apple/Documents/数据库密钥/yangkailiang",  # 私钥路径
                ssh_private_key_password="LIfeEf3kL",  # 密码（电脑开机密码）
                remote_bind_address=('rm-k2j4wjg5pl3z7h1f5.mysql.zhangbei.rds.aliyuncs.com', 3306)) as server:  # mysql服务器的address，端口号
            conn = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                                   port=server.local_bind_port,
                                   user='kuaimen_super',  # 数据库用户名
                                   passwd='super123!@#',  # 数据库密码
                                   db=mysql_name,
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor)  # 数据库名称
            cur = conn.cursor()
            cur.execute(sql)
            data = cur.fetchall()
            cur.close()
            return data

# if __name__ == '__main__':
#     # a= Mysql().select_mysql('kuaimen',"select * from team where id =1")
#     # print(a)
#     cur.execute("select * from team where id =1")
#     data = cur.fetchall()
#     print(data)
