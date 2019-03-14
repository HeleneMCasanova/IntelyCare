import sklearn.linear_model as skl
from sklearn import svm
import numpy as np
from sklearn.neural_network import MLPClassifier as mlp
import math

def run_logistic_regression(x_train, y_train, x_test, y_test):
    solvers = ['liblinear', 'newton-cg', 'lbfgs', 'sag', 'saga']
    for solve in solvers:
        print(solve)
        m = skl.LogisticRegression(solver=solve).fit(X=x_train, y=y_train)
        print(m.score(x_test, y_test))
        print(m.score(x_train, y_train))


def run_svm(x_train, y_train, x_test, y_test):
    m = svm.SVC(gamma='auto', probability=True)
    m.fit(X=x_train, y=y_train)
    a = m.score(x_test, y_test)
    b = m.score(x_train, y_train)
    return a, b

def train_svm(x_train, y_train):
    m = svm.SVC(gamma='auto', probability=True)
    m.fit(X=x_train, y=y_train)
    return m

def test_svm(m, x_test, y_test):
    a = m.score(x_test, y_test)
    return a

def run_deep_nn(x_train, y_train, x_test, y_test):
    print(len(x_train), len(x_train[0]))
    m = mlp(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(math.floor(len(x_train)/2), math.floor(len(x_train[0]) / 2)), random_state=1)
    m.fit(x_train, y_train)
    print(m.score(x_test, y_test))
