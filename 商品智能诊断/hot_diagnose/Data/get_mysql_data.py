

class Get_mysql(object):

    def __init__(self, logger, mysql):
        self.logger = logger
        self.mysql = mysql

    def get_interval_time(self, shop_id):
        '''

        :param shop_id: 店铺ID
        :return: 返回元祖（product_specific_id， 数据间隔时间）
        '''
        sql = "SELECT * FROM check_product_specific WHERE shop_id={} and operate_time =" \
              "(select MAX(operate_time) FROM check_product_specific WHERE shop_id={})".format(shop_id, shop_id)
        data = self.mysql.select_sql(sql)
        if not data:
            self.logger.logger.warning('获取店铺:{}间隔时间和product_specific_id失败，未查到数据:{}'.format(shop_id, data))
            return None, None
        product_specific_id = data[0]['id']
        interval_time = (data[0]['end_time'] - data[0]['start_time']).days + 1
        self.logger.logger.info('获取店铺:{}间隔时间和product_specific_id成功:间隔时间:{},product_specific_id:{}'.format(shop_id, interval_time, product_specific_id))
        return product_specific_id, interval_time

    def get_all_data(self, shop_id):
        '''
        获取指定店铺的最新全量数据
        :param shop_id: 店铺ID
        :return: 店铺的最新全量数据(列表)
        '''
        product_specific_id = self.get_interval_time(shop_id)[0]
        sql = "select * from check_product_info where product_specific_id={}".format(product_specific_id)
        data = self.mysql.select_sql(sql)
        if not data:
            self.logger.logger.warning('获取店铺:{}数据失败，未查到数据'.format(shop_id))
            return None
        self.logger.logger.info('获取店铺:{}数据成功,共{}条'.format(shop_id, len(data)))
        return data

    def get_layered_setting(self):
        sql = "select * FROM check_layer_setting where id=(SELECT layer_setting_id FROM check_setting_version where option_type=1 and status=1)"
        data = self.mysql.select_sql(sql)
        if not data:
            self.logger.logger.warning('获取分层、优良中差设置失败,未查到数据:{}'.format(data))
            return None
        self.logger.logger.info('获取分层、优良中差设置成功,一层访客量指数分指标量:{},三层访客指标量:{},优秀表现指数分:{},良好表现指数分:{},及格表现指数分:{}'.format(
            data[0]['first_layer_visitor_base'], data[0]['third_layer_visitor_base'], data[0]['perfect_base'], data[0]['great_base'], data[0]['pass_base']))
        return data[0]


if __name__ == '__main__':
    from hot_diagnose.Tools.Mysql import Mysql
    from hot_diagnose.Tools.Generate_log import Logger
    logger1 = Logger()
    mysql1 = Mysql(environment='test', mysql_name='saas_hot_diagnose', logger=logger1)
    obj = Get_mysql(logger=logger1, mysql=mysql1)
    # data1 = obj.get_interval_time('3591')
    # print(data1)
    data1 = obj.get_all_data(3591)
    data2 = obj.get_layered_setting()
    mysql1.close()