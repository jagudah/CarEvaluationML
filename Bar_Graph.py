from Arrayify import *
import numpy as np
import matplotlib.pyplot as plt
def addLabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

class main():
    attributes = {} #create diction, one with the attribute and the other with the count
    myData = data("Car_Data.csv")
    for index in range(len(myData)):
        if myData[index].safety in attributes: # Check if class is in the dictionary
            attributes[myData[index].safety] = attributes.get(myData[index].safety,0) + 1 # if so add 1
        else:
            attributes[myData[index].safety] = 1 #if not make it
    Xvalues = list(attributes.keys()) #x values are the attribute class
    Yvalues = list(attributes.values()) #y values are the count
    plt.bar(Xvalues,Yvalues, color = 'green',width = .4) #Create bar graph
    addLabels(Xvalues,Yvalues) 
    plt.xlabel("Safety") #label bar graph
    plt.ylabel("# of cars")
    plt.title("How safe is this car?")
    plt.show() #show bar graph
    print(attributes) #test to make sure the dictionary shows the same as the graph
