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

def rule_human(row):
    if row == 'human':
        return 1
    else:
        return 0
def rule_robot(row):
    if row == 'robot':
        return 1
    else:
        return 0
row_data = list(data['whoAmI'])
convert_rows_human = list(rule_human(el) for el in row_data)
convert_rows_robot = list(rule_robot(el) for el in row_data)

res_data = pd.DataFrame({"human": convert_rows_human, "robot": convert_rows_robot})
print("one hot вид")
print(res_data)
