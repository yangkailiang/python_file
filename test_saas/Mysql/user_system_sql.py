from Tools.Mysql import Mysql


# 根据姓名获取ID
def get_salesman_id(name, log):
    sql = "SELECT id FROM team_member where name='{}'".format(name)
    mysql = Mysql('kuaimen', log)
    data = mysql.select_sql(sql)
    mysql.close()
    if data == ():
        return None
    else:
        return data[0]['id']


#






if __name__ == '__main__':
    pass
    # from Tools.Generate_log import Logger
    # print(get_salesman_id('刘叶叶', Logger()))
    # logger = Logger()
    # Mysql('kuaimen', logger)
    # Mysql('kuaimen_order', logger)
