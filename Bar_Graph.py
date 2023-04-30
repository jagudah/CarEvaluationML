from Arrayify import *
import numpy as np
import matplotlib.pyplot as plt
def addLabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

class main():
    labels = labels("Car_Data.csv")
    for string in labels:
        print(string + "\n")
    """attributes = {}
    myData = data("Car_Data.csv")
    for index in range(len(myData)):
        if myData[index].lugboat in attributes:
            attributes[myData[index].lugboat] = attributes.get(myData[index].lugboat,0) + 1
        else:
            attributes[myData[index].lugboat] = 1
    Xvalues = list(attributes.keys())
    Yvalues = list(attributes.values())
    plt.bar(Xvalues,Yvalues, color = 'blue',width = .6)
    addLabels(Xvalues,Yvalues)
    plt.xlabel("Size of luggage in each car")
    plt.ylabel("# of cars")
    plt.title("Luggage size fit?")
    plt.show()


    print(attributes)"""
