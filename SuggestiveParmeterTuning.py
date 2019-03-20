import numpy as np
import mlpython as ml
import sklearn.preprocessing as norm
import math
import pickle
from sklearn import svm
from matplotlib import pyplot as plt
from multiprocessing import Pool

def parameterTuning():
    m = pickle.load(open('SVMmodel.sav', 'rb'))

    input = np.array([17, 6, -.08865, 84.248, 1, 4])

    input = np.reshape(input, (1, 6))
    notice = input[0][3]
    print(m.predict_proba(input))
    x = m.predict_proba(input)
    if x[0][1] < .95:
        working_params = []
        best = x[0][1]
        best_params = input
        for i in range(25):
            for j in range(24):
                for k in range(-15, 15):
                        input[0][0] = i
                        input[0][1] = j
                        input[0][2] = k/100
                        input[0][3] = notice
                        x = m.predict_proba(input)
                        if x[0][1] > best:
                            best = x[0][1]
                            best_params = input
                        if x[0][1] > .96:
                            working_params.append(input)
                            print(input)
    print("Best Params" + str(best_params))
    return best_params


if __name__ == '__main__':
    try:
        pool = Pool(4)
        pt = parameterTuning()
        data_outputs = pool.map(parameterTuning, [])
    finally:
        pool.close()
        pool.join()