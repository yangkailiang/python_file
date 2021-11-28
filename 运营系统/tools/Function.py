

def login(environment):
    import requests
    if environment == 'test':
        url = 'http://yunying-test.kmwl1688.com/api/member/login'
        data = {'phone': "admin", 'password': "12345678a"}
        res = requests.post(url=url, json=data)
        return res.cookies
    elif environment == 'prod':
        url = 'http://yunying.kmwl1688.com/api/member/login'
        data = {'phone': "17633641290", 'password': "12345678a"}
        res = requests.post(url=url, json=data)
        return res.cookies
    else:
        return '环境未能识别'
