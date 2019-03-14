import numpy as np
import pandas as pd

x = pd.read_csv('Data/IntelyCareData.csv')
bos = []
cvg = []
phl = []
pit = []
pvd = []
for i, row in x.iterrows():
    if 'BOS' in row['Market']:
        bos.append(list(row))
    if 'CVG' in row['Market']:
        cvg.append(list(row))
    if 'PHL' in row['Market']:
        phl.append(list(row))
    if 'PIT' in row['Market']:
        pit.append(list(row))
    if 'PVD' in row['Market']:
        pvd.append(list(row))

columns = ['ID','Market','CareTime','DateCreated','StartTime','Hours','TimeOfDay','NurseType','NurseTypeLabel','TimeAccepted',
           'Status','StatusTime','CNA','RN','LPN','Price','SurvivalTime','NoticeGiven','DayOfWeek','DayOfWeekValue','Weekend',
           'MarketNum', 'Survival/Notice Ratio', 'StartTimeNorm', 'HoursNorm', 'PriceNorm', 'NoticeGivenNorm', 'DayOfWeekNorm', 'MarketNorm', 'PCA']
bos = pd.DataFrame(data=bos, columns=columns)
bos.to_csv('Data/BOS.csv')
cvg = pd.DataFrame(data=cvg, columns=columns)
cvg.to_csv('Data/CVG.csv')
phl = pd.DataFrame(data=phl, columns=columns)
phl.to_csv('Data/PHL.csv')
pit = pd.DataFrame(data=pit, columns=columns)
pit.to_csv('Data/PIT.csv')
pvd = pd.DataFrame(data=pvd, columns=columns)
pvd.to_csv('Data/PVD.csv')