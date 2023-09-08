#Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

"""
list_1 = [1, 2, 3, 4, 5]
k = 3

counter = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        counter += 1
print(counter)
"""
# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
list_1 = [1, 2, 3, 4, 5, 8, 14]
k = 15
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
# мой вариант
result = list_1[0]
for i in range(1, len(list_1)):
    if k >= list_1[i]:
        result = list_1[i]
print(result)