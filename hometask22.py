""""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
 Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
lst_1 = []
lst_2 = []
n = int(input('Enter n: '))
m = int(input('Enter m: '))
for i in range(n-1):
    nums = int(input('Enter elements: '))
    lst_1.append(nums)
print(lst_1)
for i in range(m-1):
    nums = int(input('Enter elements: '))
    lst_2.append(nums)
print(lst_2)
new_lst = sorted(set(lst_1 + lst_2))
print(new_lst)