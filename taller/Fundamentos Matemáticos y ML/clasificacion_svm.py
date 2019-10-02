# -*- coding: utf8 -*-
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

iris = pd.read_csv(url, names=["SL", "SW", "PL", "PW", "F"])

print(iris.sample(5))

# Matriz de características (numérica)
X = pd.DataFrame({
    "SL": iris["SL"],
    "SW": iris["SW"],
    "PL": iris["PL"],
    "PW": iris["PW"],
})

# Vector de clases (númerico)
Y = iris["F"].map({
    "Iris-virginica": 1,
    "Iris-versicolor": 2,
    "Iris-setosa": 3,
})

from sklearn.svm import SVC

# Creamos un clasificador basado en la técnica de Vectores de Soporte
clf = SVC(gamma="scale")

# Entrenamos el clasificador
clf.fit(X, Y)

# Predecimos que familias tendrían las siguientes muestras
print(clf.predict([
    [5, 2.3, 3.6, 1.8],
    [4.7, 3.2, 1.5, 0.4],
    [7, 3.1, 5.6, 2.5],
]))

from sklearn.neural_network import MLPClassifier

# Creamos un clasificador basado en la técnica de Vectores de Soporte
clf = MLPClassifier(hidden_layer_sizes=(4, 8, 8, 3), solver='lbfgs')

# Entrenamos el clasificador
clf.fit(X, Y)

# Predecimos que familias tendrían las siguientes muestras
print(clf.predict([
    [5, 2.3, 3.6, 1.8],
    [4.7, 3.2, 1.5, 0.4],
    [7, 3.1, 5.6, 2.5],
]))