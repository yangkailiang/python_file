import datetime
from Tools.tools import division_list
from Tools.Mysql import Mysql
def bill_mysql_data(shop_id,date):
    sql = ("select * FROM shop_bill WHERE bill_date ='%s' and shop_id = %d "%(date,shop_id))
    data = Mysql().select_mysql(mysql_name='kuaimen_order',sql = sql)
    if data ==():
        return (0,0,0,0)
    else:
        sales=data[0]['sales']
        supple_amoun = data[0]['supple_amount']
        sum = sales+supple_amoun
        return data[0]['id'],sum,data[0]['supple_amount'],data[0]['normal_order_num']


def bill_mysql_refund(list_order_id):
    list_return_sale = []
    list_return_sale1 = []
    if list_order_id == []:
        list_return_sale.append(0)
    else:
        list = division_list(list_order_id,100)

        for i in list:
            if len(i) == 1:
                order = i[0]
                sql = ("SELECT order_id,refund_no,refund_payment,gmt_completed,refund_carriage FROM order_refund WHERE order_id in (%s) AND status = 'refundsuccess'"%order)
            else:
                sql = ("SELECT order_id,refund_no,refund_payment,gmt_completed,refund_carriage FROM order_refund WHERE order_id in {} AND status = 'refundsuccess'".format(tuple(i)))
            data2 = Mysql().select_mysql(mysql_name='kuaimen_order',sql=sql)
            #
            # if type == 1:
            #     if data2 != ():
            #         data = data2[0]
            #         if data['gmt_completed'] !=None:
            #             str = data['gmt_completed'].strftime("%Y-%m-%d %H:%M:%S")
            #             data1 = {data['order_id']:[data['refund_no'], data['refund_payment']/1000, str]}
            #             list_return_dict.append(data1)
            #         else:
            #             list_return_dict.append({data['order_id']:[data['refund_no'], data['refund_payment']/1000, data['gmt_completed']]})
            #     elif data2 == ():
            #         pass
            #     else:
            #         list_return_dict.append('报错了')
            #     return list_return_dict

            if data2 != ():
                data = data2[0]
                list_return_sale.append(data['refund_payment'])
                list_return_sale1.append(data['refund_carriage'])
            else:
                list_return_sale.append(0)
                list_return_sale1.append(0)
    # print(list_return_sale)
    # print(list_return_sale1)
    # return sum(list_return_sale)/100 - sum(list_return_sale1)/100
    return sum(list_return_sale)/100


def bill_order_info(order_id):
    str1 = str(order_id)
    num = str1[len(str1)-1:len(str1)]
    surface_name = 'order_info_' + num
    sql = "SELECT status,order_type FROM %s WHERE id = %d"%(surface_name,int(order_id))
    data = Mysql().select_mysql(mysql_name='kuaimen_order', sql=sql)
    try:
        return_data = {order_id : [data[0]['status'],data[0]['order_type']]}
        return return_data
    except:
        return {order_id : data}













if __name__ == '__main__':
    # a = bill_mysql_data(2,'2020-10')
    # print(a)
    b= bill_mysql_refund(['1919055313213213459', '1919056285026213459', '1918766737301997535', '1911479366550608628', '1915059996629103503'])
    print(b)
    # c = bill_order_info(1898269815170722112)
    # print(c)

