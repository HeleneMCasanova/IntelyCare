import numpy as np
import datetime as dt
import csv


list_one = []
list_two = []



with open('rate_overview_sample.csv') as csvfile:
    read_csv = csv.DictReader(csvfile, delimiter=',')
    
    for row in read_csv:
        s = row['DateCreated']
        slashCount = 0
        year = ''
        month = ''
        day = ''
        hour = ''
        min = ''
        for c in s:
            if c == '/' or c == ' ' or c == ':':
                slashCount += 1
            else:
                if slashCount == 0:
                    month += c
                elif slashCount == 1:
                    day += c
                elif slashCount == 2:
                    year += c
                elif slashCount == 3:
                    hour += c
                elif slashCount == 4:
                    min += c
        start = dt.datetime(year=int(year) + 2000, month=int(month), day=int(day), hour=int(hour), minute=int(min))

        s = row['FinalStatusTime']
        slashCount = 0
        year = ''
        month = ''
        day = ''
        hour = ''
        min = ''
        for c in s:
            if c == '/' or c == ' ' or c == ':':
                slashCount += 1
            else:
                if slashCount == 0:
                    month += c
                elif slashCount == 1:
                    day += c
                elif slashCount == 2:
                    year += c
                elif slashCount == 3:
                    hour += c
                elif slashCount == 4:
                    min += c
        end = dt.datetime(year=int(year) + 2000, month=int(month), day=int(day), hour=int(hour), minute=int(min))

        list_one.append((end-start).total_seconds())
        list_two.append(row['ShiftTimeID'])


print(len(list_one))
print(len(list_two))


list_one = np.asarray(list_one).astype(np.float)
list_two = np.asarray(list_two).astype(np.float)

correlation = np.corrcoef(list_one, list_two)[0,1]



print(correlation)