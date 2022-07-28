from ArrayGenerator import ArrayGenerator
from linearSearch import LinearSearch
import datetime

dataSize = [100000, 1000000] # 比较两个不同规模数据量下，线性查找法需要的时间
for n in dataSize:
    data = ArrayGenerator.generate_order_array(n) # 产生一组数
    startTime = datetime.datetime.now()
    # print(startTime)
    for i in range(0, 100):  # 查找的功能实现100次
        LinearSearch.search(data, n)
    endTime = datetime.datetime.now()
    # print(endTime)
    time = (endTime - startTime).total_seconds() # /1000000.0  # 获取运算的时间差，单位：秒
    print('n = {}, 100 runs: {} s'.format(n, time))