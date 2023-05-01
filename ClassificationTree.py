from Arrayify import *
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import tree
class main:
    myData = data("Car_Data.csv")
    numbs = convertToNumbers(myData)
    labels = GivenLabels("Car_Data.csv")
    labels = replaceLabels(labels)
    train = trainingData(numbs)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(train,labels)
    fig = plt.figure(figsize=(25,20))
    tree.plot_tree(clf,feature_names=["Cost","Maintence cost","Doors","Seat","Luggage Size","Safety"],class_names=["unacc","acc","good","vgood"],filled=True)
    fig.savefig("CarDecisionTree2.png")
    myTree = tree.export_text(clf)
    print(myTree)
#What should be our training vs testing samples. The data sheet is like sorted so how to do the training vs Testing samples
#Creation of 2D array yada yada