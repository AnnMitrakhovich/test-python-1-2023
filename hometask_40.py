# Задача 40:
# Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома(median_house_value), где кол-во людей от 0 до 500 (population).
import pandas as pd

data = pd.read_csv('california_housing_train.csv')

res_len = len(data[data['population'] < 500]['median_house_value'])
res_sum = data[data['population'] < 500]['median_house_value'].sum()
res = int(res_sum / res_len)
print(res_len, res_sum, res)