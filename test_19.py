"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

list_new = list()
n = int(input("Введите число N "))
for i in range(1, n+1):
    list_new.append(i)
print(list_new)
k = int(input('Число k '))

""" вариант 1
list_changed = list_new[k:] + list_new[:k]
print(list_changed) """
# вариант 2 через цикл
"""
for i in range(k):
    for j in range(len(list_new) - 1):
        temp = list_new[j]
        list_new[j] = list_new[j + 1]
        list_new[j + 1] = temp
print(list_new)"""

# вариант 3 через методы pop и insert
for i in range(k + 1, n+1):
    temp = list_new.pop()
    list_new.insert(0, temp)
print(list_new)