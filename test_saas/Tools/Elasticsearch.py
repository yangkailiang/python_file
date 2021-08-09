import os
import sys
from elasticsearch import Elasticsearch
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ES(object):
    def __init__(self, logger):
        self.__logger = logger

    def get_es_data(self, index, query):
        from Tools.tools import get_path, open_yml
        config = open_yml(get_path('config'), self.__logger)
        try:
            '''连接es       http_auth=('用户名', '密码')'''
            es = Elasticsearch(hosts=config['host'],http_auth=(config['user'], config['es_pwd']), port=config['port'], timeout=20)
            self.__logger.logger.info('连接es成功')
            '''获取查询到的数据     index为ES的索引，body为查询语句'''
            allDoc = es.search(index=index, body=query,scroll='5m',size=10000)
            results = allDoc['hits']['hits']
            total = allDoc['hits']['total']['value']    # es查询出的结果总量
            self.__logger.logger.info('查询成功，共计%s条数据'%total)
            scroll_id = allDoc['_scroll_id']            # 游标用于输出es查询出的所有结果
            for i in range(0, int(total / 100) + 1):
                # scroll参数必须指定否则会报错
                query_scroll = es.scroll(scroll_id=scroll_id, scroll='5m')['hits']['hits']
                results += query_scroll
            return results
        except Exception as e:
            self.__logger.logger.error('es查询失败，原因是：%s'%e)


if __name__ == '__main__':
    from Generate_log import *
    query = {
        "query": {
            "term": {
                "hostname": "xxx"
            }
        }
    }
    es = ES(Logger())
    a = es.get_es_data('kuaimen_order', query)
    print(a)