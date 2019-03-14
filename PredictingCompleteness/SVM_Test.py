import numpy as np
import MLModels as ml
import sklearn.preprocessing as norm
import math
markets = ['BOS', 'CVG', 'PHL', 'PIT', 'PVD']
print("With days")
test_avgs = [0 for i in range(len(markets))]
for z in range(100):
    x_train = []
    y_train = []
    x_test = [[] for i in range(len(markets))]
    y_test = [[] for i in range(len(markets))]
    for j in range(len(markets)):
        train_avg = 0
        test_avg = 0
        i = 0
        x = np.loadtxt('Data/' + str(markets[j]) + '.csv', delimiter=',', skiprows=1, dtype=str)
        np.random.shuffle(x)
        for row in x:
            i += 1
            if (i % 15) != 0:
                if row[10] == 'Completed':
                    y_train.append(1)
                    x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]), float(row[20]),
                                    float(row[8]), float(row[21])])
                if row[10] == 'Incompleted':
                    y_train.append(0)
                    x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]), float(row[20]),
                         float(row[8]), float(row[21])])
            else:
                if row[10] == 'Completed':
                    y_test[j].append(1)
                    x_test[j].append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]), float(row[20]),
                                    float(row[8]), float(row[21])])
                if row[10] == 'Incompleted':
                    y_test[j].append(0)
                    x_test[j].append([float(row[4]), float(row[5]), float(row[15]), float(row[17]), float(row[19]), float(row[20]),
                                    float(row[8]), float(row[21])])
    m = ml.train_svm(x_train, y_train)
    for k in range(len(x_test)):
        a = ml.test_svm(m, x_test[k], y_test[k])
        test_avgs[k] += a
print(test_avgs)


test_avg = 0
x = np.loadtxt('Data/IntelyCareData.csv', delimiter=',', skiprows=1, dtype=str)

for z in range(100):
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    i = 0
    np.random.shuffle(x)
    for row in x:
        i += 1
        if (i % 15) != 0:
            if row[10] == 'Completed':
                y_train.append(1)
                x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]), float(row[20]),
                                float(row[8]), float(row[21])])
            if row[10] == 'Incompleted':
                y_train.append(0)
                x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]), float(row[20]),
                                float(row[8]), float(row[21])])
        else:
            if row[10] == 'Completed':
                y_test.append(1)
                x_test.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]), float(row[20]),
                                float(row[8]), float(row[21])])
            if row[10] == 'Incompleted':
                y_test.append(0)
                x_test.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]), float(row[20]),
                                float(row[8]), float(row[21])])
    m = ml.train_svm(x_train, y_train)
    a = ml.test_svm(m, x_test, y_test)
    test_avg += a
print(test_avg)

print("Without days")
test_avgs = [0 for i in range(len(markets))]
for z in range(100):
    x_train = []
    y_train = []
    x_test = [[] for i in range(len(markets))]
    y_test = [[] for i in range(len(markets))]
    for j in range(len(markets)):
        train_avg = 0
        test_avg = 0
        i = 0
        x = np.loadtxt('Data/' + str(markets[j]) + '.csv', delimiter=',', skiprows=1, dtype=str)
        np.random.shuffle(x)
        for row in x:
            i += 1
            if (i % 15) != 0:
                if row[10] == 'Completed':
                    y_train.append(1)
                    x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                                    float(row[8]), float(row[21])])
                if row[10] == 'Incompleted':
                    y_train.append(0)
                    x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                         float(row[8]), float(row[21])])
            else:
                if row[10] == 'Completed':
                    y_test[j].append(1)
                    x_test[j].append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                                    float(row[8]), float(row[21])])
                if row[10] == 'Incompleted':
                    y_test[j].append(0)
                    x_test[j].append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                                    float(row[8]), float(row[21])])
    m = ml.train_svm(x_train, y_train)
    for k in range(len(x_test)):
        a = ml.test_svm(m, x_test[k], y_test[k])
        test_avgs[k] += a
print(test_avgs)


test_avg = 0
x = np.loadtxt('Data/IntelyCareData.csv', delimiter=',', skiprows=1, dtype=str)

for z in range(100):
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    i = 0
    np.random.shuffle(x)
    for row in x:
        i += 1
        if (i % 15) != 0:
            if row[10] == 'Completed':
                y_train.append(1)
                x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                                float(row[8]), float(row[21])])
            if row[10] == 'Incompleted':
                y_train.append(0)
                x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                                float(row[8]), float(row[21])])
        else:
            if row[10] == 'Completed':
                y_test.append(1)
                x_test.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                                float(row[8]), float(row[21])])
            if row[10] == 'Incompleted':
                y_test.append(0)
                x_test.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),
                                float(row[8]), float(row[21])])
    m = ml.train_svm(x_train, y_train)
    a = ml.test_svm(m, x_test, y_test)
    test_avg += a
print(test_avg)


print("With weekend")
test_avgs = [0 for i in range(len(markets))]
for z in range(100):
    x_train = []
    y_train = []
    x_test = [[] for i in range(len(markets))]
    y_test = [[] for i in range(len(markets))]
    for j in range(len(markets)):
        train_avg = 0
        test_avg = 0
        i = 0
        x = np.loadtxt('Data/' + str(markets[j]) + '.csv', delimiter=',', skiprows=1, dtype=str)
        np.random.shuffle(x)
        for row in x:
            i += 1
            if (i % 15) != 0:
                if row[10] == 'Completed':
                    y_train.append(1)
                    x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]), float(row[20]),
                                    float(row[8]), float(row[21])])
                if row[10] == 'Incompleted':
                    y_train.append(0)
                    x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]), float(row[20]),
                         float(row[8]), float(row[21])])
            else:
                if row[10] == 'Completed':
                    y_test[j].append(1)
                    x_test[j].append([float(row[4]), float(row[5]), float(row[15]), float(row[17]), float(row[20]),
                                    float(row[8]), float(row[21])])
                if row[10] == 'Incompleted':
                    y_test[j].append(0)
                    x_test[j].append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),  float(row[20]),
                                    float(row[8]), float(row[21])])
    m = ml.train_svm(x_train, y_train)
    for k in range(len(x_test)):
        a = ml.test_svm(m, x_test[k], y_test[k])
        test_avgs[k] += a
print(test_avgs)


test_avg = 0
x = np.loadtxt('Data/IntelyCareData.csv', delimiter=',', skiprows=1, dtype=str)

for z in range(100):
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    i = 0
    np.random.shuffle(x)
    for row in x:
        i += 1
        if (i % 15) != 0:
            if row[10] == 'Completed':
                y_train.append(1)
                x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[20]),
                                float(row[8]), float(row[21])])
            if row[10] == 'Incompleted':
                y_train.append(0)
                x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]), float(row[20]),
                                float(row[8]), float(row[21])])
        else:
            if row[10] == 'Completed':
                y_test.append(1)
                x_test.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]), float(row[20]),
                                float(row[8]), float(row[21])])
            if row[10] == 'Incompleted':
                y_test.append(0)
                x_test.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]), float(row[20]),
                                float(row[8]), float(row[21])])
    m = ml.train_svm(x_train, y_train)
    a = ml.test_svm(m, x_test, y_test)
    test_avg += a
print(test_avg)



print("With only days")
test_avgs = [0 for i in range(len(markets))]
for z in range(100):
    x_train = []
    y_train = []
    x_test = [[] for i in range(len(markets))]
    y_test = [[] for i in range(len(markets))]
    for j in range(len(markets)):
        train_avg = 0
        test_avg = 0
        i = 0
        x = np.loadtxt('Data/' + str(markets[j]) + '.csv', delimiter=',', skiprows=1, dtype=str)
        np.random.shuffle(x)
        for row in x:
            i += 1
            if (i % 15) != 0:
                if row[10] == 'Completed':
                    y_train.append(1)
                    x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]),
                                    float(row[8]), float(row[21])])
                if row[10] == 'Incompleted':
                    y_train.append(0)
                    x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]),
                         float(row[8]), float(row[21])])
            else:
                if row[10] == 'Completed':
                    y_test[j].append(1)
                    x_test[j].append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]),
                                    float(row[8]), float(row[21])])
                if row[10] == 'Incompleted':
                    y_test[j].append(0)
                    x_test[j].append([float(row[4]), float(row[5]), float(row[15]), float(row[17]), float(row[19]),
                                    float(row[8]), float(row[21])])
    m = ml.train_svm(x_train, y_train)
    for k in range(len(x_test)):
        a = ml.test_svm(m, x_test[k], y_test[k])
        test_avgs[k] += a
print(test_avgs)


test_avg = 0
x = np.loadtxt('Data/IntelyCareData.csv', delimiter=',', skiprows=1, dtype=str)

for z in range(100):
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    i = 0
    np.random.shuffle(x)
    for row in x:
        i += 1
        if (i % 15) != 0:
            if row[10] == 'Completed':
                y_train.append(1)
                x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]),
                                float(row[8]), float(row[21])])
            if row[10] == 'Incompleted':
                y_train.append(0)
                x_train.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]),
                                float(row[8]), float(row[21])])
        else:
            if row[10] == 'Completed':
                y_test.append(1)
                x_test.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]),
                                float(row[8]), float(row[21])])
            if row[10] == 'Incompleted':
                y_test.append(0)
                x_test.append([float(row[4]), float(row[5]), float(row[15]), float(row[17]),float(row[19]),
                                float(row[8]), float(row[21])])
    m = ml.train_svm(x_train, y_train)
    a = ml.test_svm(m, x_test, y_test)
    test_avg += a
print(test_avg)