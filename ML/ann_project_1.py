# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:36:56 2022

@author: bisht
"""

#ann_project_1

#import libraries
import numpy as np
import pandas as pd
import tensorflow as tf
import os

#import dataset
os.chdir(r'E:/programming/dataset/')
data = pd.read_csv('Churn_Modelling.csv')

#data preprocessing
x=data.iloc[:,3:-1].values
y=data.iloc[:,-1].values

#Label encoding of Gender column
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
x[:,2]=le.fit_transform(x[:,2])

#OneHotEncoding of Geography column
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct= ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[1])], remainder='passthrough')
x=ct.fit_transform(x)

#spliting data into test and train set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#feature scaling or enhancing
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

#creating ANN
ann=tf.keras.models.Sequential()
ann.add(tf.keras.layers.Dense(units=6,activation='relu'))   #hidden layer 1
ann.add(tf.keras.layers.Dense(units=6,activation='relu'))   #hidden layer 2
ann.add(tf.keras.layers.Dense(units=11,activation='relu'))
ann.add(tf.keras.layers.Dense(units=1,activation='sigmoid'))    #outputlayer

#compling model
ann.compile(optimizer='adam',loss='binary_crossentropy',metrics='accuracy')

#training ANN
ann.fit(x_train,y_train,batch_size=32,epochs=100)

#predict for single input
#print(ann.predict(sc.transform([[1,0,0,600,1,40,3,60000,2,1,1,50000]])) > 0.5)

#test ANN on test set
y_pred=ann.predict(x_test)
y_pred=(y_pred > 0.5)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

#making Confusion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))

#display confusion  matrix
from sklearn.metrics import ConfusionMatrixDisplay
disp=ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
