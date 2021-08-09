import requests

from requests.packages import urllib3
def get_data(shop_id):


    url_login = 'https://saas.tmz1688.com/api/manage/user/login'
    login_data = {'username': "17633641290", 'password': "wWr1KC7964"}
    urllib3.disable_warnings()
    login = requests.post(url_login, json = login_data, verify = False)

    token = login.json()['data']['token']
    header = {'Authorization': token}

    # url_day = 'https://saas.tmz1688.com/api/saas/check/product/getLastTime'
    # data_day = {'shopId': shop_id}
    # r_day = requests.post(url_day, headers = header, json = data_day, verify = False).json()

    url_shop = 'https://saas.tmz1688.com/api/saas/check/product/pageList'
    shop_data = {'shopId': shop_id, 'current': 1, 'pageSize': 2000}
    r_shop = requests.post(url_shop, headers=header, json=shop_data, verify = False).json()
    # if r_day['data']['days'] == 7:
    #     for i in r_shop['data']['records']:
    #         if i['visitorCount'] > 1000:
    #             return r_shop,True
    #         else:
    #             return r_shop,False
    # elif r_day['data']['days'] == 30:
    #     for i in r_shop['data']['records']:
    #         if i['visitorCount'] > 4000:
    #             return r_shop,True
    #         else:
    #             return r_shop,False
    return r_shop
if __name__ == '__main__':
    data = get_data(1037)
    # print(data)
    print(data)
    # for i in data:
    #     print(i)\