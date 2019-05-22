#import numpy as np
import pandas as pd
"""with open('projet.xlsx', 'rb') as f:
    content = f.readlines()
file = pd.read_csv('Données.csv', sep=";")
print(file[0:3])
file = pd.read_excel('Données.xlsx', 'Données')
print(file[:])"""
file = pd.read_excel('Données.xlsx', 'Moyenne')
print(file[0:36])
file = pd.read_excel('Données.xlsx', 'Age')
print(file[0:43])
file = pd.read_excel('Données.xlsx', 'Globales2')
print(file[0:3])
#file.to_excel("ll.xlsx")

