import numpy as np
import pandas as pd
import datetime as dt
import lifelines as lf
from matplotlib import pyplot as plt
import math

x = pd.read_csv('Data\IntelyCareData.csv')

km_data = [[[], []] for i in range(10)] #2d array to store surival time and censored/uncensored label for market types
for i, row in x.iterrows():
    if row['Status'] == 'Completed':
        if row['Market'] == 'BOS-Cape':
            km_data[0][0].append(int(row['SurvivalTime']))
            km_data[0][1].append(1)
        if row['Market'] == 'BOS-North':
            km_data[1][0].append(int(row['SurvivalTime']))
            km_data[1][1].append(1)
        if row['Market'] == 'BOS-South':
            km_data[2][0].append(int(row['SurvivalTime']))
            km_data[2][1].append(1)
        if row['Market'] == 'BOS-West':
            km_data[3][0].append(int(row['SurvivalTime']))
            km_data[3][1].append(1)
        if row['Market'] == 'CVG-1':
            km_data[4][0].append(int(row['SurvivalTime']))
            km_data[4][1].append(1)
        if row['Market'] == 'PHL-1':
            km_data[5][0].append(int(row['SurvivalTime']))
            km_data[5][1].append(1)
        if row['Market'] == 'PHL-2':
            km_data[6][0].append(int(row['SurvivalTime']))
            km_data[6][1].append(1)
        if row['Market'] == 'PIT-1':
            km_data[7][0].append(int(row['SurvivalTime']))
            km_data[7][1].append(1)
        if row['Market'] == 'PSM-1':
            km_data[8][0].append(int(row['SurvivalTime']))
            km_data[8][1].append(1)
        if row['Market'] == 'PVD-1':
            km_data[9][0].append(int(row['SurvivalTime']))
            km_data[9][1].append(1)

    if row['Status'] == 'Deleted':
        if row['Market'] == 'BOS-Cape':
            km_data[0][0].append(int(row['SurvivalTime']))
            km_data[0][1].append(0)
        if row['Market'] == 'BOS-North':
            km_data[1][0].append(int(row['SurvivalTime']))
            km_data[1][1].append(0)
        if row['Market'] == 'BOS-South':
            km_data[2][0].append(int(row['SurvivalTime']))
            km_data[2][1].append(0)
        if row['Market'] == 'BOS-West':
            km_data[3][0].append(int(row['SurvivalTime']))
            km_data[3][1].append(0)
        if row['Market'] == 'CVG-1':
            km_data[4][0].append(int(row['SurvivalTime']))
            km_data[4][1].append(0)
        if row['Market'] == 'PHL-1':
            km_data[5][0].append(int(row['SurvivalTime']))
            km_data[5][1].append(0)
        if row['Market'] == 'PHL-2':
            km_data[6][0].append(int(row['SurvivalTime']))
            km_data[6][1].append(0)
        if row['Market'] == 'PIT-1':
            km_data[7][0].append(int(row['SurvivalTime']))
            km_data[7][1].append(0)
        if row['Market'] == 'PSM-1':
            km_data[8][0].append(int(row['SurvivalTime']))
            km_data[8][1].append(0)
        if row['Market'] == 'PVD-1':
            km_data[9][0].append(int(row['SurvivalTime']))
            km_data[9][1].append(0)


markets = ['BOS-Cape', 'BOS-North', 'BOS-South', 'BOS-West', 'CVG-1', 'PHL-1', 'PHL-2', 'PIT-1', 'PSM-1', 'PVD-1']
i = 0
for market in km_data:
    if market[1] == []:
        continue
    m = lf.KaplanMeierFitter()
    m.fit(durations=market[0], event_observed=market[1], label=markets[i])
    if i ==0:
        ax = m.survival_function_.plot()
    else:
        m.survival_function_.plot(ax=ax)
    i+=1
plt.show()