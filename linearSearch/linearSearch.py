class LinearSearch:
    @staticmethod
    def search(data, target):
        for i in range(0, len(data)):
            if data[i] == target:
                return i
        return -1
'''
    def __init__(self, data):
        self.data = data


    def search(self,target):
        for i in range(0,len(self.data)):
            if self.data[i] == target:
                return i
        return -1

data = [24, 18, 12, 9, 16, 66, 32, 4]
ls = LinearSearch(data)
res = ls.search(16)
print(res)
res2 = ls.search(666)
print(res2)
'''

