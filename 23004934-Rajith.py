# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 00:10:49 2024

@author: RAJITH N
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

dataset= pd.read_csv("drug-overdose-death-rates new.csv")

#dataset analysis
print(dataset.shape)
print(dataset.columns)
dataset.info()
dataset.isnull().sum()
dataset=dataset.dropna()
dataset.head(10)
dataset= dataset.drop(['Entity','Code'], axis='columns')
dataset.head(5)

dataset.describe()

def line():
    plt.plot(dataset['Year'][:10],dataset['Any opioid death rates (CDC WONDER)'][:10] , color='orange')
    plt.xlabel("Year")
    plt.ylabel("Opioid death rate")
    plt.title("Drug Opioid overdose death rate")
    plt.legend()
    plt.show()
line()

def histo():
    plt.figure(figsize=(10,10))
    plt.hist(dataset['Prescription Opioids death rates (US CDC WONDER)'],bins=50,color='blue')
    plt.xlabel("prescribed opioids death rate")
    plt.ylabel("death rate")
    plt.title("Drug overdose death rate")
    plt.show()
    histo()

def barplot():
    plt.figure(figsize=(10,10))
    plt.bar(dataset['Year'][:10],dataset['Heroin overdose death rates (CDC WONDER)'][:10],color='green')
    plt.xlabel("Year")
    plt.title("Drug heroin overdose death rate")
    plt.show()
    barplot()
    
heatmap_dataset = dataset[['Any opioid death rates (CDC WONDER)', 
                        'Cocaine overdose death rates (CDC WONDER)',
                        'Heroin overdose death rates (CDC WONDER)',
                        'Synthetic opioids death rates (CDC WONDER)',
                        'Prescription Opioids death rates (US CDC WONDER)']]

correlation_matrix = heatmap_dataset.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap of drugs death rate')
plt.show()

line()
barplot()
histo()
heatmap_dataset
    plt.figure(figsize=(10,10))
    plt.bar(dataset['Year'][:10],dataset['Heroin overdose death rates (CDC WONDER)'][:10],color='green')
    plt.xlabel("Year")
    plt.title("Drug heroin overdose death rate")
    plt.show()