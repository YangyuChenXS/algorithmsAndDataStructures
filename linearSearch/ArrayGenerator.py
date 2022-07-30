import random

class ArrayGenerator:
    @staticmethod
    def generate_order_array(n):
        # 生成一组整数：从0到n-1
        arr = []
        for i in range(0, n):
            arr.append(i)
        return arr

    @staticmethod
    def generate_random_array(n,bound):
        # 生成一组随机数，其中有n个数组，且数据范围在[0,bound)之间
        arr = []
        for i in range(0, n):
            arr.append(random.uniform(0, bound))
        return arr








