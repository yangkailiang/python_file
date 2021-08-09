
import pytest
import allure
import pytest_check
from Get_data.get_es_data import *
from Get_data.get_yunying_data import *
@allure.feature('测试运营后台与ES中的数据是否准确')
class Test_chect():
    shop_id = Zhanbao_api().shop_service('2',400)
    @allure.story('运营战报-单个店铺与es中数据核验')
    @allure.severity('critical')
    @allure.description('通过接口获取战报里的数据，和es查询到的数据做对比')
    @allure.step('参数')
    # @pytest.mark.P0
    @pytest.mark.parametrize('shop_id',shop_id[0],ids =shop_id[1])
    def test_shop(self,shop_id):
        starttime = "2021-07-01 00:00:00"
        endtime = "2021-07-30 23:59:59"
        data_yunying = Zhanbao_api().zhanbao_shop(shop_id,starttime,endtime)
        data_es=get_es_data(shop_id,starttime,endtime)
        es_net_sale = int(sum([i for i in data_es.values()]))
        pytest_check.equal(int(data_yunying['net_sale']),es_net_sale,print('查询时间范围：%s---%s\n运营系统净销售额：%s\nes中的销售额：%s'%(starttime,endtime,int(data_yunying['net_sale']),es_net_sale)))









if __name__ == '__main__':
    pass
    # os.system('pytest --alluredir ./report/allure_raw')
    # print(os.system('allure serve report/allure_raw'))
# pytest --alluredir ./report/allure_raw