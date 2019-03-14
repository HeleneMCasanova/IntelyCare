import numpy as np
import MLModels as ml
import sklearn.preprocessing as norm
import math
import pickle
from sklearn import svm
from matplotlib import pyplot as plt


markets = ['BOS', 'CVG', 'PHL', 'PIT', 'PVD']
x_train = []
y_train = []
x = np.loadtxt('Data\IntelyCareData.csv', delimiter=',', skiprows=1, dtype=str)
for row in x:
    if row[10] == 'Completed':
        y_train.append(1)
        x_train.append(
            [float(row[4]), float(row[5]), float(row[15]), float(row[17]),
             float(row[8]), float(row[21])])
    if row[10] == 'Incompleted':
        y_train.append(0)
        x_train.append(
            [float(row[4]), float(row[5]), float(row[15]), float(row[17]),
             float(row[8]), float(row[21])])


'''
m = ml.train_svm(x_train, y_train)
pickle.dump(m, open('Data/SVMmodel.sav', 'wb'))
'''
m = pickle.load(open('Data/SVMmodel.sav', 'rb'))
z = []
y = []
#for j in range(52, 102):
correct = 0
count = 0
for j in range(55, 100):
    for i in range(len(x_train)):
        x = np.array(x_train[i])
        x = np.reshape(x, (1, 6))
        if (m.predict_proba(x)[0][1] < (j/100)) and (m.predict_proba(x)[0][1] > ((j/100)-.05)):
            count+=1
            if y_train[i] == 1:
                correct +=1
    z.append(correct/count)
    print(correct/count)


plt.plot(range(55, 100), z)
plt.ylabel('Prediction Accuracy')
plt.xlabel('Confidence (%)')
plt.title('Prediction Accuracy by confidence on Completed shifts')
plt.show()