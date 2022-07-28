class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        '''
        这里相当于重写了相等方法的判断，并且也会影响 ==
        '''
        return self.name == other.name
        #return self.name.lower() == other.name.lower() # 忽略大小写

