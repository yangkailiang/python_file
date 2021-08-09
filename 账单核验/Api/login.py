from Tools.tools import *

class Api(object):
    def __init__(self):
        url = open_yml(get_path(''))
    def zhanbao_department(self,starttime,endtime):
        '''
        战报-组织-大部门  （运营一部、运营二部、运营三部）
        :param start_time: 开始时间（精确到秒）
        :param endtime: 结束时间（精确到秒）
        :return: json
        '''
        url = self.yml['zhanbao_department']
        data = {"startTime": starttime, "endTime": endtime}
        data = super().post(self.login,url,data)
        return data


    @try_except
    @get_zhanbao_data_list
    def zhanbao_shop(self,shop_id,starttime,endtime):
        '''
        战报内的单个店铺的数据
        :param shop_id: 店铺id
        :param endtime: 结束时间
        :param start_time: 开始时间
        :return: json
        '''
        url = self.yml['zhanbao_shop']
        data = {'achiveSort': 'true',
                'current': 1,
                'endTime': endtime,
                'pageSize': 20,
                'shopId': shop_id,
                'startTime': starttime}
        data = super().post(self.login,url,data)
        return data


    @try_except
    @get_shop_id_list
    def shop_service(self,status,size):
        '''
        获取店铺管理内的列表
        :param status: 店铺状态
        :param size: 多少行数据
        :return: 接口返回（json）
        '''
        url = self.yml['shop_service']
        data = {'commissionRateOrder': "",
                'current': 1,
                'endOrder': "",
                'jobType': "",
                'pageSize': size,
                'startOrder': "",
                'status': status,
                'surplusDaysOrder': "",
                'tradeMedalOrder': ""}
        data = super().post(self.login,url,data)
        return data


    def bill_sale(self,bill_id,status,pages):
        url = self.yml['bill_sale']
        data = {'billId': bill_id,
                'current': pages,
                'dropType': 0,
                'keyword': "",
                'orderType': status,
                'pageSize': 1000,
                'signType': "",
                'time': []}
        return super().post(self.login,url,data)

