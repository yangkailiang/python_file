
def deviation_publicity(max_value, min_value, value):
    if max_value - min_value == 0:
        return 0
    deviation = (value - min_value) / (max_value - min_value)
    return deviation


def calculation(lst):
    offline_transaction_amount_lst = [value['线下交易金额'] for value in lst]
    offline_transaction_num_lst = [value['线下交易单数'] for value in lst]
    max_offline_transaction_amount = max(offline_transaction_amount_lst)
    min_offline_transaction_amount = min(offline_transaction_amount_lst)
    max_offline_transaction_num = max(offline_transaction_num_lst)
    min_offline_transaction_num = min(offline_transaction_num_lst)
    for value in lst:
        value['线下交易金额分值'] = deviation_publicity(max_offline_transaction_amount, min_offline_transaction_amount, value['线下交易金额']) * 0.7
        value['线下交易单数分值'] = deviation_publicity(max_offline_transaction_num, min_offline_transaction_num, ['线下交易单数']) * 0.3
        value['款式来源分值'] = value['自主开发'] * 0.7 + value['整合'] * 0.3

    for value in lst:
        is_standard_product = value['标品']
        visitor = value['访客']
        achievement = value['业绩']
        promotion_cost = value['推广费用']
        company_strength = value['公司实力']
        merchant_strength = value['商家实力']
        new_frequency = value['上新频率']

        if is_standard_product == '标品':
            if visitor < 100:
                value['访客分值'] = 20
            elif 100 <= visitor < 300:
                value['访客分值'] = 40
            elif 300 <= visitor < 600:
                value['访客分值'] = 60
            elif 600 <= visitor < 1000:
                value['访客分值'] = 80
            elif 1000 <= visitor:
                value['访客分值'] = 100

            if new_frequency == 0:
                value['上新频率分值'] = 0
            elif new_frequency == 1:
                value['上新频率分值'] = 20
            elif 2 <= new_frequency <= 5:
                value['上新频率分值'] = 40
            elif 6 <= new_frequency <= 10:
                value['上新频率分值'] = 60
            elif 11 <= new_frequency <= 30:
                value['上新频率分值'] = 80
            elif 31 <= new_frequency:
                value['上新频率分值'] = 100

        elif is_standard_product == '非标品':
            if visitor < 300:
                value['访客分值'] = 20
            elif 300 <= visitor < 600:
                value['访客分值'] = 40
            elif 600 <= visitor < 1200:
                value['访客分值'] = 60
            elif 1200 <= visitor < 3000:
                value['访客分值'] = 80
            elif 3000 <= visitor:
                value['访客分值'] = 100

            if new_frequency == 0:
                value['上新频率分值'] = 0
            elif 1 <= new_frequency <= 19:
                value['上新频率分值'] = 20
            elif 20 <= new_frequency <= 39:
                value['上新频率分值'] = 40
            elif 40 <= new_frequency <= 59:
                value['上新频率分值'] = 60
            elif 60 <= new_frequency <= 80:
                value['上新频率分值'] = 80
            elif 81 <= new_frequency:
                value['上新频率分值'] = 100

        if achievement < 50000:
            value['业绩分值'] = 10
        elif 50000 <= achievement < 200000:
            value['业绩分值'] = 20
        elif 200000 <= achievement < 500000:
            value['业绩分值'] = 40
        elif 50000 <= achievement < 1000000:
            value['业绩分值'] = 60
        elif 100000 <= achievement < 2000000:
            value['业绩分值'] = 80
        elif 2000000 <= achievement:
            value['业绩分值'] = 100

        if promotion_cost < 3000:
            value['推广费用分值'] = 20
        elif 3000 <= promotion_cost < 9000:
            value['推广费用分值'] = 40
        elif 9000 <= promotion_cost < 15000:
            value['推广费用分值'] = 60
        elif 15000 <= promotion_cost < 30000:
            value['推广费用分值'] = 80
        elif 30000 <= promotion_cost:
            value['推广费用分值'] = 100

        if company_strength < 10000000:
            value['公司实力分值'] = 20
        elif 10000000 <= company_strength < 30000000:
            value['公司实力分值'] = 40
        elif 30000000 <= company_strength < 60000000:
            value['公司实力分值'] = 60
        elif 60000000 <= company_strength < 100000000:
            value['公司实力分值'] = 80
        elif 100000000 <= company_strength:
            value['公司实力分值'] = 100

        if merchant_strength == '普通商家':
            value['商家实力分值'] = 40
        elif merchant_strength == '实力商家':
            value['商家实力分值'] = 60
        elif merchant_strength == '超级工厂' or merchant_strength == 'ka':
            value['商家实力分值'] = 80
        elif merchant_strength == 'ska':
            value['商家实力分值'] = 100\

    return lst


def calculation_score(lst):
    final_lst = []
    for value in lst:
        operation_index = value['访客分值'] * 0.1 + value['业绩分值'] * 0.3 + value['推广费用分值'] * 0.2 \
                          + value['上新频率分值'] * 0.1 + value['线下交易金额分值'] * 0.1 + \
                          value['线下交易单数分值'] * 0.1 + value['款式来源分值'] * 0.1
        potential_index = value['推广费用分值'] * 0.3 + + value['上新频率分值'] * 0.1 + value['款式来源分值'] * 0.2 \
                          + value['线下交易金额分值'] * 0.2 + value['线下交易单数分值'] * 0.2
        risk_index = (100 - value['访客分值']) * 0.1 + (100 - value['业绩分值']) * 0.3 + value['推广费用分值'] * 0.2 \
                     + value['上新频率分值'] * 0.1 + value['线下交易金额分值'] * 0.1 + value['线下交易单数分值'] * 0.1 \
                     + value['款式来源分值'] * 0.1
        counter_attack_index = value['访客分值'] * 0.2 + value['业绩分值'] * 0.4 + (100 - value['推广费用分值']) * 0.2 \
                               + (100 - value['线下交易金额分值']) * 0.1 + (100 - value['线下交易单数分值']) * 0.1
        final_lst.append({'operation_index': operation_index, 'potential_index': potential_index,
                          'risk_index': risk_index, 'counter_attack_index': counter_attack_index})
    return final_lst


def main(lst):
    calculation_lst = calculation(lst)
    calculation_score_lst = calculation_score(calculation_lst)
    return calculation_score_lst


if __name__ == '__main__':
    data = [{'标品': '标品', '访客': 111111, '业绩': 1232334, '推广费用': 1233234, '公司实力': 89832394894, '商家实力': '普通商家',
             '上新频率': 1333, '自主开发': 6, '整合': 4, '线下交易金额': 123232413, '线下交易单数': 1233}]
    print(main(data))