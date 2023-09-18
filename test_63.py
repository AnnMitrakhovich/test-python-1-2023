"""
Задача №63.
1. Изобразите отношение households к population с помощью точечного графика
2. Визуализировать longitude по отношения к median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('california_housing_test.csv')


def first():
    households = data.households
    population = data.population
    plt.scatter(households, population)
    plt.xlabel("households")
    plt.ylabel("population")
    plt.show()


first()

def second_point():
