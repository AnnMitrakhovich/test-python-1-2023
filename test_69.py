"""
Задача №69
1. Изобразить гистограмму по flipper_length_mm
с оттенком height_group. Сделать анализ
"""
import matplotlib.pyplot as plt
import seaborn as sns
from random import randint
penguins = sns.load_dataset("penguins")
def first():
    sns.histplot(penguins, x='flipper_length_mm', hue='species')
    plt.show()

first()