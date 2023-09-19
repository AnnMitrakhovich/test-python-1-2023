import pandas as pd

import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

final_data = pd.get_dummies(data["whoAmI"]).astype(int)
print("one hot вид")
print(final_data)


def rule(x, row):
    if x == row:
        return 1
    else:
        return 0


row_data = list(data['whoAmI'])
row_1 = "human"
convert_rows_human = list(rule(el, row_1) for el in row_data)
row_2 = "robot"
convert_rows_robot = list(rule(el, row_2) for el in row_data)

res_data = pd.DataFrame({"human": convert_rows_human, "robot": convert_rows_robot})
print("one hot вид")
print(res_data)
