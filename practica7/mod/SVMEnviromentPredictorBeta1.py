import csv
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR

dfTraining = pd.read_csv("dataset_training.csv")
dfTesting = pd.read_csv("dataset_validation.csv")

 
X_train = dfTraining[["mes","dia"]]
y_train=dfTraining.average

X_testing = dfTesting[["mes","dia"]]
y_testing = dfTesting.average

print("-------------------- Normal SVM -------------------------")

clf = SVR(C=1.0, epsilon=0.2)
clf.fit(X_train, y_train) 
SVR(C=1.0, cache_size=200, coef0=0.0,
  degree=3, gamma='auto', kernel='rbf',
  max_iter=-1,  shrinking=True,
  tol=0.001, verbose=False)
scores = cross_val_score(clf, X_train, y_train, cv = 10)
res1=clf.predict(X_testing)

print("---------------------------------------------")
index=0
for element in res1:
    error=(abs((element-y_testing[index]))/y_testing[index])*100
    print('Predicted Value: ', element, ' Real value: ', y_testing[index], " % Error: ", error)
    index=index+1
    
pathCsvfile="./outRealTesting1.csv"
with open(pathCsvfile, 'w', encoding='utf-8', newline='') as csvFile:
    fieldnames = ['predictedValue', 'RealValue','ErrorPercent']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames) 
    writer.writeheader() 
    index=0
    for element in res1:
        error=(abs((element-y_testing[index]))/y_testing[index])*100
        print('Predicted Value: ', element, ' Real value: ', y_testing[index], " % Error: ", error)
        writer.writerow({'predictedValue': "'"+format(element)+"'", 'RealValue': "'"+format(y_testing[index])+"'", 'ErrorPercent': "'"+format(error)+"'"})
        index=index+1
print("---------------------------------------------")