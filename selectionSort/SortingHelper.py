from selectionSort import SelectionSort
from selectionSort import SelecionSortHomeWork
import datetime


class SortingHelper:
    @staticmethod
    def is_sorted(arr_data):
        # 检验一组数是否排序完成，数据量太大的时候无法用打印出来用肉眼观察
        # 故比对前后数的大小即可
        length = len(arr_data)
        for i in range(0, length-1):
            if arr_data[i] > arr_data[i+1]:
                return False
        return True

    @staticmethod
    def sort_test(sortname,arr_data):
        # 根据传入的算法名，测试对应算法的执行时间
        start_time = datetime.datetime.now()
        print(start_time)
        if sortname == 'SelectionSort':
            SelectionSort.SelectionSort.selection_sort(arr_data)
        elif sortname == 'SelecionSortHomeWork':
            SelecionSortHomeWork.SelecionSortHomeWork.select_sort_reverse(arr_data)
        end_time = datetime.datetime.now()
        print(end_time)
        time = (end_time - start_time).total_seconds()  # /1000000.0  # 获取运算的时间差，单位：秒
        if SortingHelper.is_sorted(arr_data):
            print('{}  length: {} The difference of time is {} seconds'.format(sortname, len(arr_data),time))
        else:
            print('SelectionSort failed')