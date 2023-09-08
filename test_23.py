"""
Задача №23. Дан массив, состоящий из целых чисел.
Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""
lst_obj = [0, -1, 5, 2, 3, 7]
count_index = 0
for i in range(len(lst_obj) -1):
    if lst_obj[i] < lst_obj[i+1]:
        count_index += 1
print(count_index)