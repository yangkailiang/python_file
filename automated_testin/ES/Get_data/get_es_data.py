from time import ctime

from Ornament.ornament_es import *
# from Generate_log import generate_log
from Tools.tools import *


@try_except
@get_es_shop_data
def get_es_data(index,query):
    from elasticsearch import Elasticsearch
    '''连接es       http_auth=('用户名', '密码')'''
    es = Elasticsearch(hosts='ES-cn-6ja1wcfbt001w4ucf.public.elasticsearch.aliyuncs.com',http_auth=('yangkailiang', 'K2k3kikd'), port=9200, timeout=50000)
    '''获取查询到的数据     index为ES的索引，body为查询语句'''
    allDoc = es.search(index=index, body=query,scroll='5m',size=10000)
    results = allDoc['hits']['hits']
    total = allDoc['hits']['total']['value']    # es查询出的结果总量
    # scroll_id = allDoc['_scroll_id']            # 游标用于输出es查询出的所有结果
    # for i in range(0, int(total / 100) + 1):
    #     # scroll参数必须指定否则会报错
    #     query_scroll = ES.scroll(scroll_id=scroll_id, scroll='5m')['hits']['hits']
    #     results += query_scroll
    return results













if __name__ == '__main__':
    print(ctime())
    starttime = "2021-06-01 00:00:00"
    endtime = "2021-06-30 23:59:59"
    dict= get_es_data('3600',starttime,endtime)
    print(dict)
    print(ctime())


