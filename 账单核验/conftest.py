# pytest会先读取这个配置文件
# 这里是一个hook钩子函数的实现：在系统函数生效之前，钩子会先执行。
# 它会“勾”住函数的变量、参数。
# 继而可以改变原有的功能


#新建一个自定义标签
def pytest_configure(config):
    # 定义一个自定义标签
    config.addinivalue_line('markers','P0')   # P0是最高级别的case，必须回归
    config.addinivalue_line('markers', 'P1')  # P1大版本上线需要回归的case
    config.addinivalue_line('markers', 'P2')  # P2季度回归的case

def pytest_collection_modifyitems(items):
    for item in items:
        # item.name = item.neme.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')