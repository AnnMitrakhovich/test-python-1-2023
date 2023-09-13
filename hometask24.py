""""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать
за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки."""

lst_havest = [1, 30, 5, 0, 5, 3, 6, 10] #входной файл грядки
""" 
max_berries = 0
for i in range(1, len(lst_havest) - 1):
    berries = lst_havest[i-1] + lst_havest[i] + lst_havest[i+1]
    if berries > max_berries:
        max_berries = berries
if (lst_havest[len(lst_havest) - 2] + lst_havest[len(lst_havest) - 1] + lst_havest[0]) > max_berries:
    max_berries = (lst_havest[len(lst_havest) - 2] + lst_havest[len(lst_havest) - 1] + lst_havest[0])
if (lst_havest[len(lst_havest) - 1] + lst_havest[0] + lst_havest[1]) > max_berries:
    max_berries = (lst_havest[len(lst_havest) - 1] + lst_havest[0] + lst_havest[1])
"""
sum_berries = ([sum(lst_havest[i:i+3]) for i in range(len(lst_havest)-2)] +
               [lst_havest[len(lst_havest)-2] + lst_havest[len(lst_havest)-1] + lst_havest[0]] +
               [lst_havest[len(lst_havest)-1] + lst_havest[0] + lst_havest[1]])
max_berries = max(sum_berries)
print(max_berries)

