from Arrayify import *
import numpy as np
import matplotlib.pyplot as plt
def addLabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

class main():
    attributes = {}
    myData = data("Car_Data.csv")
    for index in range(len(myData)):
        if myData[index].safety in attributes:
            attributes[myData[index].safety] = attributes.get(myData[index].safety,0) + 1
        else:
            attributes[myData[index].safety] = 1
    Xvalues = list(attributes.keys())
    Yvalues = list(attributes.values())
    plt.bar(Xvalues,Yvalues, color = 'green',width = .4)
    addLabels(Xvalues,Yvalues)
    plt.xlabel("Safety")
    plt.ylabel("# of cars")
    plt.title("How safe is this car?")
    plt.show()
    print(attributes)
