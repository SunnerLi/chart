from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style="darkgrid")

def addValue():
    ax = plt.gca()
    for p in ax.patches:
        x_coor = p.get_width()
        y_coor = p.get_y() + p.get_height() / 2.
        ax.text(x_coor, y_coor, int(x_coor))

def getZeroBar(color):
    if color == None:
        exit()
    return plt.bar(0, 0, color=color)

df = pd.read_csv('council.csv')

# Compute Stack value
df['total'] = df['female'] + df['male']
df = df.drop('female', 1)
print(df)

# Draw
sns.barplot(x='total', y='area', data=df, color='c')
sns.barplot(x='male', y='area', data=df, color='g')
addValue()
plt.legend((getZeroBar('c'), getZeroBar('g')), ['Male', 'Female'])
plt.show()