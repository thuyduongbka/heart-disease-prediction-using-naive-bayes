# import pandas as pd
# import matplotlib.pyplot as plt
# import random
# file = pd.read_csv('D:/data.csv',nrows=5,index_col=0)
# print(file)
# # Xem chiều dài của df, tương đương shape[0]
# print('Len:', len(file))
# # Xem thông tin dataframe vừa đọc được
# file.info()
# # Xem kích thước của dataframe
# print('Shape:', file.shape)
#print(file['age'])

import csv
ifile =  open('D:/HD/data/train/train3.csv', 'r') 
spamreader = csv.reader(ifile)

X = []
Y = []
i = 0
for row in spamreader:
    if(i>0):
        Y.append(row[len(row)-1])
        X.append(row[:-1])    
    i=1
print(len(X))
print(len(Y))

import numpy as np
X = np.array(X).astype(np.float)
Y = np.array(Y).astype(np.float)


from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
def train_model(classifier, X,Y):       
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=40)       
    classifier.fit(X_train, Y_train)            
    train_predictions = classifier.predict(X_train)
    test_predictions = classifier.predict(X_test)
      
    print('Train accuracy: ', metrics.accuracy_score(train_predictions, Y_train))    
    print("Test accuracy: ", metrics.accuracy_score(test_predictions, Y_test))
    
    print(classification_report(Y_train, train_predictions, target_names=['0','1'],digits=3))

from sklearn.naive_bayes import GaussianNB
train_model(GaussianNB(),X,Y)

