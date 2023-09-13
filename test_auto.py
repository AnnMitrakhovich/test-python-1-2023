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
"""
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
"""

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
""" 
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:

А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков."""
# Напишите программу, которая вычисляет стоимость введенного пользователем
# слова k и выводит его. Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
k = 'ноутбук'

list_1 = ['н', 'о', 'т']
list_2 = ['у', 'к', 'п']
list_3 = ['б', 'ь', 'я']
count_num = 0
for i in range(len(k)):
    if k[i] in list_1:
        count_num += 1
    elif k[i] in list_2:
        count_num += 2
    elif k[i] in list_3:
        count_num += 3
    else:
        continue
print(count_num)
"""
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count) """
