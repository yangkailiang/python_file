# from Tools.Generate_log import generate_log
from Tools.tools import *
@try_except
def get_es_shop_data(fucn):
    def es_data(shop_id,startime,endtime):
        start = split_es_date(startime)
        end = split_es_date(endtime)
        dict = {}
        query = {
            "aggs": {
                "3": {
                    "date_histogram": {
                        "field": "pay_time",
                        "calendar_interval": "1d",
                        "time_zone": "Asia/Shanghai",
                        "min_doc_count": 1
                    },
                    "aggs": {
                        "2": {
                            "sum": {
                                "field": "net_sale"
                            }
                        }
                    }
                }
            },
            "size": 0,
            "stored_fields": [
                "*"
            ],
            "script_fields": {
                "total_amount_human": {
                    "script": {
                        "source": "if (doc['total_amount'].size()>0) { return doc['total_amount'].value / 100; } else return 0;",
                        "lang": "painless"
                    }
                },
                "shipping_fee_human": {
                    "script": {
                        "source": "if (doc['shipping_fee'].size()>0) { return doc['shipping_fee'].value / 100; } else return 0;",
                        "lang": "painless"
                    }
                },
                "net_sale_human": {
                    "script": {
                        "source": "if (doc['net_sale'].size()>0) { return doc['net_sale'].value / 100; } else return 0;",
                        "lang": "painless"
                    }
                }
            },
            "docvalue_fields": [
                {
                    "field": "complete_time",
                    "format": "date_time"
                },
                {
                    "field": "create_time",
                    "format": "date_time"
                },
                {
                    "field": "pay_time",
                    "format": "date_time"
                }
            ],
            "_source": {
                "excludes": []
            },
            "query": {
                "bool": {
                    "must": [],
                    "filter": [
                        {
                            "bool": {
                                "should": [
                                    {
                                        "match_phrase": {
                                            "shop_id": shop_id
                                        }
                                    }
                                ],
                                "minimum_should_match": 1
                            }
                        },
                        {
                            "match_all": {}
                        },
                        {
                            "match_phrase": {
                                "inside_order_type": "1"
                            }
                        },
                        {
                            "range": {
                                "pay_time": {
                                    "gte": start,
                                    "lte": end,
                                    "format": "strict_date_optional_time"
                                }
                            }
                        }
                    ],
                    "should": [],
                    "must_not": [
                        {
                            "bool": {
                                "minimum_should_match": 1,
                                "should": [
                                    {
                                        "match_phrase": {
                                            "order_state": "cancel"
                                        }
                                    },
                                    {
                                        "match_phrase": {
                                            "order_state": "refundsuccess"
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        }
        data = fucn('kuaimen_order',query)
        for a in range(len(data)):
            data1 = data[a]['_source']
            if data1['net_sale'] !=None:
                dict[data[a]['_id']] = data1['net_sale']/100
            elif data1['net_sale'] ==None:
                dict[data[a]['_id']] = 0
        return dict

    return es_data

