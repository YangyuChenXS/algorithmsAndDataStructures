from SelectionSort import SelectionSort

data = [24, 18, 12, 9, 16.55, 66, 32, 4.3]
res = SelectionSort.sort_new(data)
print('占用内存的选择排序后结果为： {}'.format(res))
print('占用内存的选择排序后原数组data结果为： {}'.format(data))

res = SelectionSort.selection_sort(data)
print('原地选择排序后结果为: {}'.format(res))
print('原地选择排序后原数组data结果为: {}'.format(data))
