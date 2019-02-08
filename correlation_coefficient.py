import numpy as np
import datetime as dt
from collections import OrderedDict
import csv

def getLists(read_csv, g):
    list_one = []
    for row in read_csv:
        list_one.append(row[g])
    
    return list_one

def printResults(list_one, list_two):
    list_one = np.asarray(list_one).astype(np.float)
    list_two = np.asarray(list_two).astype(np.float)
    correlation = np.corrcoef(list_one, list_two)[0,1]
    print(correlation)
    return 0

def tg(list_one):
    newList = []
    for time in list_one:
        if time == 'ET':
            newList.append(0)
        elif time == 'DT':
            newList.append(1)
        elif time == 'WDT':
            newList.append(2)
        elif time == 'WET':
            newList.append(3)
        elif time == 'NT':
            newList.append(4)
        else:
            newList.append(5)
    #print(newList)
    return newList

def ipt(list_one):
    newList = []
    for t in list_one:
        if t == 'Nurse':
            newList.append(0)
        elif t == 'RN':
            newList.append(1)
        elif t == 'CNA':
            newList.append(2)
        else:
            newList.append(3)
    return newList

def fs(list_one):
    newList = []
    for t in list_one:
        if t == 'Deleted':
            newList.append(0)
        elif t == 'Requested':
            newList.append(1)
        else:
            newList.append(2)
    return newList

def state(list_one):
    newList = []
    for t in list_one:
        if t == 'MA':
            newList.append(0)
        elif t == 'PA':
            newList.append(1)
        elif t == 'OH':
            newList.append(2)
        else:
            newList.append(3)
    return newList

def market(list_one):
    newList = []
    for t in list_one:
        if t == 'BOS-Cape':
            newList.append(0)
        elif t == 'BOS-North':
            newList.append(1)
        elif t == 'BOS-South':
            newList.append(2)
        elif t == 'BOS-West':
            newList.append(3)
        elif t == 'CVG-1':
            newList.append(4)
        elif t == 'PHL-1':
            newList.append(5)
        elif t == 'PIT-1':
            newList.append(6)
        else:
            newList.append(7)
    return newList

def price(list_one):
    newList = []
    for t in list_one:
        if t != '':
            newList.append(t)
        else:
            newList.append(0)
    return newList


list_one = []
list_two = []

groups = ['RequestHours', 'TimeGroup', 'ShiftTimeID','IntelyProType', 'LastMinuteShift', 'Holiday', 'HolidayBilling', 'FinalStatus', 'ClientID', 'Market','State', 'ZipCode','CNA', 'LPN', 'RN', 'UserGroup', 'Price']

with open('IntelyCareData.csv') as csvfile:
    read_csv = csv.DictReader(csvfile, delimiter=',')
    list_two = getLists(read_csv, 'newDuration')
    
    for g in groups:
        csvfile.seek(0)
        print(g)

        list_one = getLists(read_csv, g)
        list_one.pop(0)
        
        if g == 'TimeGroup':
            list_one = tg(list_one)
        if g == 'IntelyProType':
            list_one = ipt(list_one)
        if g == 'FinalStatus':
            list_one = fs(list_one)
        if g == 'State':
            list_one = state(list_one)
        if g == 'Market':
            list_one = market(list_one)
        if g == 'Price':
            list_one = price(list_one)

        printResults(list_one, list_two)

        list_one = []