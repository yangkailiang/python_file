

# 导入模块
from collections import Iterable

# 通过isinstance方法来判断该对象是否能迭代
# 用法 isinstance(要判断的对象，Iterable)
# 返回Ture则可以，返回Fales则不可以
isinstance([1,2,3], Iterable)

# 判断该是实列对象是否是该类创建的
# 1. 创建一个test类
class test():
    def add(self):
        pass

# 2.创建test类的实列对象
obj = test()
# 3. 判断obj实列对象是否是通过test类创建的
# 3.1 用法： isinstance(实列对象, 类)
#     返回Ture则可以，返回Fales则不可以
bool = isinstance(obj, test)
print(bool)