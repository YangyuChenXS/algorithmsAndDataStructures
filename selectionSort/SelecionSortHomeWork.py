from selectionSort import SelectionSort


class SelecionSortHomeWork:
    @staticmethod
    def select_sort_reverse(arr_data):
        # SelecionSort.select_sort中实现的选择排序是从前向后排序
        # 这里从后向前排序，也就是
        # arr[i..n]已排序，arr[0...i]未排序
        length = len(arr_data)
        for i in range(length-1, -1, -1):
            max_index = i
            for j in range(max_index, -1, -1):
                if arr_data[max_index] < arr_data[j]:
                    SelectionSort.SelectionSort.swap(arr_data, max_index, j)
        return arr_data


