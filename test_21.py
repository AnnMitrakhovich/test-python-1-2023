"""
Задача №21. Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
lst_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
         {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "},
         {" VIII ": " S007 "}]
# вариант 1
# создаем множество
set_obj = set()
# для каждого словаря в списке создаем элемент множества из значений словаря values
for dict_els in lst_1:
    for vals in dict_els.values():
        set_obj.add(vals)
print(set_obj)

# вариант 2
#
set_obj = set(val for dict_el in lst_1 for val in dict_el.values())
print(set_obj)