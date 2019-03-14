import numpy as np
import MLModels as ml
import sklearn.preprocessing as norm
import math
import pickle
from sklearn import svm
from matplotlib import pyplot as plt

m = pickle.load(open('Data/SVMmodel.sav', 'rb'))



markets = ['BOS', 'CVG', 'PHL', 'PIT', 'PVD']
x_train = []
y_train = []
complete = 0
incomplete = 0
z_svm = []
z = []
x = np.loadtxt('Data\IntelyCareData.csv', delimiter=',', skiprows=1, dtype=str)

for j in range(24):
    complete = 0
    incomplete = 0
    svm_complete = 0
    svm_incomplete = 0
    for row in x:
        if (float(row[4]) <= j) and (float(row[4]) > (j-3)):
            y = np.array([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                                    float(row[8]), float(row[21])])
            y = np.reshape(y, (1, 6))
            if row[10] == 'Completed':
                complete+=1
            if row[10] == 'Incompleted':
                incomplete+=1
            if m.predict(y) == 1:
                svm_complete += 1
            else:
                svm_incomplete += 1

    if complete+incomplete !=0:
        z.append(complete/(incomplete+complete))
        z_svm.append(svm_complete/(svm_incomplete+svm_complete))

plt.plot(z, label='True Completeness')
plt.ylabel('Percent Complete')
plt.xlabel('Hour of Day')
plt.title('Shift Completeness Percentage by time of day')
plt.plot(z_svm, label='SVM')
plt.show()

z = []
z_svm = []
for j in range(32):
    complete = 0
    incomplete = 0
    svm_complete = 0
    svm_incomplete = 0
    for row in x:

        if (float(row[5]) <= j) and (float(row[5]) > (j-3)):
            y = np.array([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                          float(row[8]), float(row[21])])
            y = np.reshape(y, (1, 6))
            if row[10] == 'Completed':
                complete+=1
            if row[10] == 'Incompleted':
                incomplete+=1
            if m.predict(y) == 1:
                svm_complete += 1
            else:
                svm_incomplete += 1

    if complete+incomplete !=0:
        z.append(complete/(incomplete+complete))
        z_svm.append(svm_complete/(svm_incomplete+svm_complete))
plt.plot(z, label='True Completeness')
plt.ylabel('Percent Complete')
plt.xlabel('Hours Requested')
plt.title('Shift Completeness Percentage by hours requested')
plt.plot(z_svm, label='SVM')
plt.show()

z = []
z_svm = []
for j in range(8):
    complete = 0
    incomplete = 0
    svm_complete = 0
    svm_incomplete = 0
    for row in x:
        y = np.array([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                      float(row[8]), float(row[21])])
        y = np.reshape(y, (1, 6))
        if (float(row[19]) == j):
            if row[10] == 'Completed':
                complete+=1
            if row[10] == 'Incompleted':
                incomplete+=1
            if m.predict(y) == 1:
                svm_complete += 1
            else:
                svm_incomplete += 1

    if complete+incomplete !=0:
        z.append(complete/(incomplete+complete))
        z_svm.append(svm_complete/(svm_incomplete+svm_complete))

plt.plot(z, label='True Completeness')
plt.ylabel('Percent Complete')
plt.xlabel('Day of Week')
plt.title('Shift Completeness Percentage by Day of Week')
plt.plot(z_svm, label='SVM')
plt.show()


z = []
z_svm = []
for j in range(-31, 45, 1):
    complete = 0
    incomplete = 0
    svm_incomplete = 0
    svm_complete = 0
    for row in x:
        y = np.array([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                      float(row[8]), float(row[21])])
        y = np.reshape(y, (1, 6))
        if (float(row[15]) <= j/100) and (float(row[15]) > ((j/100)-.04)):
            if row[10] == 'Completed':
                complete+=1
            if row[10] == 'Incompleted':
                incomplete+=1
            if m.predict(y) == 1:
                svm_complete += 1
            else:
                svm_incomplete += 1

    if complete+incomplete !=0:
        z.append(complete/(incomplete+complete))
        z_svm.append(svm_complete/(svm_incomplete+svm_complete))

plt.plot(range(-31, 44,), z, label='True Completeness')
plt.ylabel('Percent Complete')
plt.xlabel('Price (%)')
plt.title('Shift Completeness Percentage by Price')
plt.plot(range(-31, 44,), z_svm, label='SVM')
plt.show()


z = []
z_svm = []
for j in range(0, 122):
    complete = 0
    incomplete = 0
    svm_complete = 0
    svm_incomplete = 0
    for row in x:
        if (float(row[17]) <= j/100) and (float(row[17]) > ((j/100)-.04)):
            y = np.array([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                          float(row[8]), float(row[21])])
            y = np.reshape(y, (1, 6))
            if row[10] == 'Completed':
                complete+=1
            if row[10] == 'Incompleted':
                incomplete+=1
            if m.predict(y) == 1:
                svm_complete += 1
            else:
                svm_incomplete += 1

    if complete+incomplete !=0:
        z.append(complete/(incomplete+complete))
        z_svm.append(svm_complete/(svm_incomplete+svm_complete))

plt.plot(range(0, 121), z, label='True Completeness')
plt.ylabel('Percent Complete')
plt.xlabel('Notice Given (Days)')
plt.title('Shift Completeness Percentage by Notice Given')
plt.plot(z_svm, label='SVM')
plt.show()


z = []
z_svm = []
for j in range(2):
    complete = 0
    incomplete = 0
    svm_complete = 0
    svm_incomplete = 0
    for row in x:
        y = np.array([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                      float(row[8]), float(row[21])])
        y = np.reshape(y, (1, 6))
        if (float(row[20]) == j):
            if row[10] == 'Completed':
                complete+=1
            if row[10] == 'Incompleted':
                incomplete+=1
            if m.predict(y) == 1:
                svm_complete += 1
            else:
                svm_incomplete += 1

    if complete+incomplete !=0:
        z.append(complete/(incomplete+complete))
        z_svm.append(svm_complete/(svm_incomplete+svm_complete))
y = ["Weekday", 'Weekend']
plt.scatter(y, z, label='True Completeness')
plt.ylabel('Percent Complete')
plt.xlabel('Weekday/Weekend')
plt.title('Shift Completeness Percentage by weekend/weekday')
plt.scatter(y, z_svm, label='SVM')
plt.show()


z = []
z_svm = []
for j in range(2):
    complete = 0
    incomplete = 0
    svm_complete = 0
    svm_incomplete = 0
    for row in x:
        y = np.array([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                      float(row[8]), float(row[21])])
        y = np.reshape(y, (1, 6))
        if (float(row[8]) == j):
            if row[10] == 'Completed':
                complete+=1
            if row[10] == 'Incompleted':
                incomplete+=1
            if m.predict(y) == 1:
                svm_complete += 1
            else:
                svm_incomplete += 1

    if complete+incomplete !=0:
        z.append(complete/(incomplete+complete))
        z_svm.append(svm_complete/(svm_incomplete+svm_complete))
y = ["CNA", 'Nurse']
plt.scatter(y, z, label='True Completeness')
plt.ylabel('Percent Complete')
plt.xlabel('Nurse Type')
plt.title('Shift Completeness Percentage by nurse type')
plt.scatter(y, z_svm, label='SVM')
plt.show()



z = []
z_svm = []
for j in range(1,6):
    complete = 0
    incomplete = 0
    svm_complete = 0
    svm_incomplete = 0
    for row in x:
        y = np.array([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                      float(row[8]), float(row[21])])
        y = np.reshape(y, (1, 6))
        if (float(row[21]) == j):
            if row[10] == 'Completed':
                complete+=1
            if row[10] == 'Incompleted':
                incomplete+=1
            if m.predict(y) == 1:
                svm_complete += 1
            else:
                svm_incomplete += 1

    if complete+incomplete !=0:
        z.append(complete/(incomplete+complete))
        z_svm.append(svm_complete/(svm_incomplete+svm_complete))
y = ['BOS', 'CVG', 'PHL', 'PIT', 'PVD']
plt.scatter(y, z, label='True Completeness')
plt.ylabel('Percent Complete')
plt.xlabel('Market')
plt.title('Shift Completeness Percentage by Market')
plt.scatter(y, z_svm, label='SVM')
plt.show()
