from Arrayify import *
import numpy as np
import matplotlib.pyplot as plt
class main():
    labels = labels("Car_Data.csv")
    for string in labels:
        print(string + "\n")
    myData = data("Car_Data.csv")
    numbs = convertToNumbers(myData)
    for item in numbs:
        print(item.buying, end=" ")
        print(item.maint,end= " ")
        print(item.doors,end= " ")
        print(item.persons,end= " ")
        print(item.lugboat,end= " ")
        print(item.safety,end= " ")