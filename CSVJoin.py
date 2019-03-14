import pandas as pd
import numpy as np

x = pd.read_csv('fff.csv')
y = pd.read_csv('zzz.csv')


z = pd.merge(x, y, how='left', left_on='A', right_on='A')
z.to_csv('ddd.csv')

'''
z = []
num = 0
i = 0
for h, row in x.iterrows():
    if int(row['RequestId']) == num:
        print('wrgiuwg')
    else:
        z.append(list(row))
        print('hmmm')
        num = int(row['RequestId'])
    i+=1
z = pd.DataFrame(data=z)
print(z)
z.to_csv('zzz.csv')
'''

