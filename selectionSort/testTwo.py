from linearSearch import ArrayGenerator
from selectionSort import SortingHelper


# 比较不同数据量的选择排序的执行时间
data_size = [1000, 10000]
for n in data_size:
    arr_data = ArrayGenerator.ArrayGenerator.generate_random_array(n, n)
    SortingHelper.SortingHelper.sort_test('SelectionSort', arr_data)
    
for n in data_size:
    arr_data = ArrayGenerator.ArrayGenerator.generate_random_array(n, n)
    SortingHelper.SortingHelper.sort_test('SelecionSortHomeWork', arr_data)






