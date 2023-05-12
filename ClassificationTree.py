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
    clf = tree.DecisionTreeClassifier(max_depth=6) #run the decision tree classifier
    clf = clf.fit(train,labels)
    fig = plt.figure(figsize=(25,20))
    tree.plot_tree(clf,feature_names=["Cost","Maintence cost","Doors","Seat","Luggage Size","Safety"],class_names=["unacc","acc","good","vgood"],filled=True) #tree figure
    fig.savefig("CarDecisionTree2.png")
    myTree = tree.export_text(clf) #changed the tree into text as well
    print(clf.predict([[1,1,3,3,2,3],[1,1,3,2,2,3]]))
    print(myTree)