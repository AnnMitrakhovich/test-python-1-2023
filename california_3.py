"""
1. Определить какое максимальное и минимальное
значение median_house_value
2. Показать максимальное median_house_value, где
median_income = 3.1250
3. Узнать какая максимальная population в зоне
минимального значения median_house_value
"""
import pandas as pd
data = pd.read_csv('california_housing_test.csv')
print(f'{data["median_house_value"].min()} - минимальное, {data["median_house_value"].max()} - максимальное значение median_house_value')