from joblib import load

clf = load('clf.joblib') 

print(clf.predict([
    [1, 1, 1, 1],
    [2, 2, 2, 2],
]))