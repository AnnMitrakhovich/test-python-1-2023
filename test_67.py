"""
Задача №67
1. Создать новый столбец в таблице с пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:
penguins = sns.load_dataset("penguins")
penguins.head()
"""
import seaborn as sns
from random import randint
penguins = sns.load_dataset("penguins")

def func(row):
    res = randint(1, 60)
    val = None
    if res < 35:
        val = "low"
    elif 35 < res < 43:
        val = "middle"
    elif res > 42:
        val = "high"
    return val
penguins["len"] = penguins.apply(func, axis=1)
print(penguins)
