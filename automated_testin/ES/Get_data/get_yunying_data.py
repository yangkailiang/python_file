import requests
from Ornament.ornament_yunying import *
from Tools.tools import *
class Post_method(object):
    @try_except
    def post(self,r,url,data):
        '''
        post请求类
        :param r: session对象（需要获取登录状态的接口）
        :param url: url
        :param data: 参数（json格式）
        :return: 响应信息（json格式）
        '''
        response = r.post(url,json=data,timeout = 100).json()
        return response


    @try_except
    def login(self):
        '''
        获取登录状态，账号已写死
        :return: 登录后的session对象
        '''
        url = self.yml['login']
        data = {'password': "wWr1KC7964",'phone': "17633641290"}
        r = requests.session()
        r.post(url,json=data).json()
        return r



class Zhanbao_api(Post_method):
    def __init__(self):
        self.yml = open_yml('/Users/apple/python项目/automated_testin/ES/Data/url.yaml')
        self.login = super().login()
    @try_except
    @get_zhanbao_department_data
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

if __name__ == '__main__':

    # a = Zhanbao_api().zhanbao_department("2021-06-01 00:00:00","2021-06-06 23:59:59")
    # # (['运营三部', '运营一部', '运营二部'],{'销售额': [8291041.68, 10352028.93, 4695790.26], '可提佣销售额': [2082688.26, 2015612.54, 1446522.31]})
    # print(a)
    # b = Zhanbao_api().shop_service('2',10)
    # print(b)
    # print('ccccc')
    # c = Zhanbao_api().zhanbao_shop(1078,"2021-06-01 00:00:00","2021-06-06 23:59:59")
    # print(c)
    # bill = Zhanbao_api().bill_sale(10731,'1',3)
    # print(bill)
    # starttime = "2021-06-02 00:00:00"
    # endtime = "2021-06-30 23:59:59"
    # data = Zhanbao_api().bill_sale(10700,'1',1)
    # print(data)
    a = Post_method().login()
    print(a)