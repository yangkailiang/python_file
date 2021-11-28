import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from apscheduler.schedulers.blocking import BlockingScheduler
from tools.Mysql import Mysql
from tools.Generate_log import Logger
from tools.Dingding import Dingding
logger = Logger()
mysql = Mysql(environment='prod', mysql_name='kuaimen_shop', logger=logger)
dingding = Dingding(logger=logger)


def member_lst():
    # 培训销售
    sql1 = "SELECT * FROM `kuaimen`.`team_member` WHERE `team_post_id` IN (27) AND `joy_status` = '1' AND `status` = '1'"
    # 销售专员
    sql2 = "SELECT * FROM `kuaimen`.`team_member` WHERE `team_post_id` IN (16) AND `joy_status` = '1' AND `status` = '1'"
    data1 = mysql.select_sql(sql1)
    data2 = mysql.select_sql(sql2)

    train_lst = sorted([i['id'] for i in data1])
    operate_lst = sorted([i['id'] for i in data2])
    return train_lst, operate_lst


def judge():
    try:
        sql1 = "SELECT count(*) as num, member_id FROM `kuaimen_shop`.`shop_clue_train` WHERE `member_id` IS NOT NULL and is_assignable=1 and data_status=0 GROUP BY member_id"
        sql2 = "SELECT count(*) as num, member_id FROM `kuaimen_shop`.`shop_clue_operate` WHERE `member_id` IS NOT NULL and is_assignable=1 and data_status=0 GROUP BY member_id"
        data1 = mysql.select_sql(sql1)
        data2 = mysql.select_sql(sql2)
        lst = member_lst()
        train_lst = sorted([i['member_id'] for i in data1])
        operate_lst = sorted([i['member_id'] for i in data2])
        if lst[0] == train_lst:
            dingding.send_dingding_msg('爬虫项目', '培训销售:分配人员列表与 成员列表相同')
        else:
            dingding.send_dingding_msg('爬虫项目', '培训销售:分配人员列表与 成员列表不相同:{},{}'.format(lst[0], train_lst))
        if lst[1] == operate_lst:
            dingding.send_dingding_msg('爬虫项目', '销售专员:分配人员列表与 成员列表相同')
        else:
            dingding.send_dingding_msg('爬虫项目', '销售专员:分配人员列表与 成员列表不相同:{},{}'.format(lst[1], operate_lst))

        for value in data1:
            if value['num'] <= 5:
                sql = "SELECT * FROM `kuaimen`.`team_member` WHERE `id` = {}".format(value['member_id'])
                data = mysql.select_sql(sql)
                dingding.send_dingding_msg('爬虫项目', '{}线索小于5条'.format(data[0]['name']))
            elif value['num'] > 25:
                sql = "SELECT * FROM `kuaimen`.`team_member` WHERE `id` = {}".format(value['member_id'])
                data = mysql.select_sql(sql)
                dingding.send_dingding_msg('爬虫项目', '{}线索大于25条'.format(data[0]['name']))
            else:
                pass
        for value in data2:
            if value['num'] <= 5:
                sql = "SELECT * FROM `kuaimen`.`team_member` WHERE `id` = {}".format(value['member_id'])
                data = mysql.select_sql(sql)
                dingding.send_dingding_msg('爬虫项目', '{}线索小于5条'.format(data[0]['name']))
            elif value['num'] > 25:
                sql = "SELECT * FROM `kuaimen`.`team_member` WHERE `id` = {}".format(value['member_id'])
                data = mysql.select_sql(sql)
                dingding.send_dingding_msg('爬虫项目', '{}线索大于25条'.format(data[0]['name']))
            else:
                pass
    except Exception as e:
        dingding.send_dingding_msg('爬虫项目', '报错了：{}'.format(e))

judge()
# scheduler = BlockingScheduler()
# scheduler.add_job(judge, 'cron', day_of_week='1-6', hour=17, minute=25)
# scheduler.start()
mysql.close()