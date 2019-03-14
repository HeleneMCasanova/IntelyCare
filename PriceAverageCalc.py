import numpy as np
import pandas as pd
import datetime as dt
import lifelines as lf
from matplotlib import pyplot as plt
import math

x = pd.read_csv('ddd.csv')

lpn = 0
lpncount = 0
cn = 0
cncount = 0
rn = 0
rncount = 0
nurse = 0
nursecount = 0

small = 0
eh = 0
ok = 0
big =0
smallinc = 0
ehinc = 0
okinc = 0
biginc = 0
for i, row in x.iterrows():

    if row['NurseType'] == 'CNA':
        if float(row['CNA']) != 0 and not math.isnan(float(row['CNA'])):
            cn += float(row['CNA'])
            cncount += 1
    if row['NurseType'] == 'Nurse':
        if float(row['RN']) != 0 and not math.isnan(float(row['RN'])):
            rn += float(row['RN'])
            rncount += 1
    if row['NurseType'] == 'Nurse':
        if float(row['LPN']) != 0 and not math.isnan(float(row['LPN'])):
            lpn += float(row['LPN'])
            lpncount += 1

print(cn/cncount)
print((rn/rncount))
print((rn/rncount + lpn/lpncount)/2)
print(lpn/lpncount)


