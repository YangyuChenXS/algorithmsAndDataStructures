class SelectionSort:
    @staticmethod
    def sort_new(data):
        # 选择排序，但是不改变原来的数组，将数组重排后，保存在新数组里面
        # 缺点：新开辟了一个数组，占用内存
        arr_data = data[:]  # 不能直接使用 arr_data = data；否则赋值的只是列表，会造成一旦arr_data发生改变,data也会发生改变
        arr = []
        n = len(arr_data)
        for i in range(0,n):
            length = len(arr_data)
            for j in range(0,length):
                if arr_data[0] > arr_data[j]:
                    SelectionSort.swap(arr_data,0,j)
            arr.append(arr_data[0])
            arr_data.pop(0)
        return arr

    @staticmethod
    def selection_sort(data):
        # 选择排序，但是是在直接在原来的数组中进行排序，返回排序好的数组，不占用新内存
        length = len(data)
        # 循环不变量: data[0..i]是有序的，data[i...n]是无序的
        for i in range(0, length):
            min_index = i
            for j in range(min_index, length):
                if data[min_index] > data[j]:
                    SelectionSort.swap(data, min_index,j)
        return data

    @staticmethod
    def swap(data, i, j):
        temp = data[j]
        data[j] = data[i]
        data[i] = temp
