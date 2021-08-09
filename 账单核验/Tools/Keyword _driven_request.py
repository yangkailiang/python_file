
import requests
# def judge_content_type():


# def judge_response():
#
#
#
#
#
# def request(data):
#     if data['method'] == 'get':








# def multiple_request(yml_data):
#     for all_case in yml_data:
#         for num in range(len(yml_data[all_case]['request'])):
#             if num < len(yml_data[all_case]['request']) - 1:
#
#
#
#
#         for case in yml_data[all_case]['request']:
#             num = len(yml_data[all_case]['request'])
#             data_request = yml_data[all_case][case + '_data']
#
#             print(case, data_request)















if __name__ == '__main__':
    url= 'http://web.juhe.cn:8080/constellation/getAll'
    data1 = {'consName':'处女座','type':'today','key':'d396cbdfc011a1d2851b8680860dae01'}
    header = {'Content-Type': 'text/html'}
    data = requests.get(url, data1, headers=header).json()
    print(data)
