
import yaml

import pytest

def login(a):

    return a[0]+a[1]
def test(b):
    return b[1]+b[0]
with open('/Users/ykl/test_saas/Configuration_file/aaa.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
func = data['data']['func']
print(data)


class Test_case():
    for i in len(data):
        def test1(self):
            for i in range(len(func)):
                if i < len(func) - 1:
                    eval(func[i])(data[i]['data']['data'][i])
                elif i == len(func) - 1:
                    data1 = eval(func[i])(data[i]['data']['data'][i])
                    assert data1 == 1
    # eval(i)(data['data']['test'])