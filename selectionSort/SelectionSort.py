class SelectionSort:

    @staticmethod
    def sort_new(data):
        # 选择排序，但是不改变原来的数组，将数组重排后，保存在新数组里面
        # 缺点：新开辟了一个数组，占用内存
        arr_data = data
        arr = []
        n = len(arr_data)
        for i in range(0,n):
            length = len(arr_data)
            for j in range(0,length):
                if arr_data[0] > arr_data[j]:
                    temp = arr_data[j]
                    arr_data[j] = arr_data[0]
                    arr_data[0] = temp
            arr.append(arr_data[0])
            arr_data.pop(0)
        return arr

