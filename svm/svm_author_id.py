#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################

clf = svm.SVC( kernel='rbf', C=10000.0 )

features_train = features_train[:len(features_train)/1] 
labels_train = labels_train[:len(labels_train)/1] 

t0 = time()
clf.fit( features_train, labels_train )
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict( features_test )
print "predition time:", round(time()-t0, 3), "s"

accuracy = clf.score ( features_test, labels_test )
print accuracy

print len( filter( lambda x: x == 1, pred ) )
