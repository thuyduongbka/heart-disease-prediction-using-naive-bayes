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


def StoI(row):
    for i in range(0,len(row)):
        row[i] = int(row[i])
    return row


import csv
ifile =  open('D:/tieu_duong.csv', 'r')
spamreader = csv.reader(ifile)

X = []
Y = []
for row in spamreader:    
        Y.append(row[len(row)-1])        
        X.append(row[:-1])    

print(len(X))
print(len(Y))

#------------------------------
from sklearn import preprocessing

encoder = preprocessing.LabelEncoder()
Y = encoder.fit_transform(Y)
#------------------------------

import numpy as np
X = np.array(X).astype(np.float)
Y = np.array(Y).astype(np.float)

from sklearn.model_selection import train_test_split
from sklearn import metrics
def train_model(classifier, X,Y):       
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=None)       
    classifier.fit(X_train, Y_train)            
    train_predictions = classifier.predict(X_train)
    test_predictions = classifier.predict(X_test)
      
    print('Train accuracy: ', metrics.accuracy_score(train_predictions, Y_train))    
    print("Test accuracy: ", metrics.accuracy_score(test_predictions, Y_test))

from sklearn.naive_bayes import GaussianNB
train_model(GaussianNB(),X,Y)

