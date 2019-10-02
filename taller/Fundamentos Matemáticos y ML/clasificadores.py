# -*- coding: utf8 -*-
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

iris = pd.read_csv(url, names=["SL", "SW", "PL", "PW", "F"])

iris = iris.sample(len(iris))

X_fit = pd.DataFrame({
    "SL": iris[0:120]["SL"],
    "SW": iris[0:120]["SW"],
    "PL": iris[0:120]["PL"],
    "PW": iris[0:120]["PW"],
})

X_test = pd.DataFrame({
    "SL": iris[120:]["SL"],
    "SW": iris[120:]["SW"],
    "PL": iris[120:]["PL"],
    "PW": iris[120:]["PW"],
})

Y_fit = iris[0:120]["F"].map({
    "Iris-virginica": 1,
    "Iris-versicolor": 2,
    "Iris-setosa": 3,
})

Y_test = iris[120:]["F"].map({
    "Iris-virginica": 1,
    "Iris-versicolor": 2,
    "Iris-setosa": 3,
})

from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(hidden_layer_sizes=(1, 2, 1))

clf.fit(X_fit, Y_fit)

Y_predict = clf.predict(X_test)

import numpy as np

diff = sum( (Y_predict - Y_test) ** 2) * 1.

print(diff)

print(Y_predict)
print(Y_test)

print(clf.coefs_)

from joblib import dump, load

dump(clf, "clf.joblib")