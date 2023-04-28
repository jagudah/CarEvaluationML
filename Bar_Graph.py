from Arrayify import *
import numpy as np
import matplotlib.pyplot as plt
class main():
    attributes = {}
    myData = data("Car_Data.csv")
    for index in range(len(myData)):
        if myData[index].doors in attributes:
            attributes[myData[index].doors] = attributes.get(myData[index].doors,0) + 1
        else:
            attributes[myData[index].doors] = 1
            


    print(attributes)
