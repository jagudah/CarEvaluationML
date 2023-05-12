'''This file was for testing the best way to understand the file, and convert into dataframe/array'''
from Arrayify import *
import numpy as np
import matplotlib.pyplot as plt
class main():
    '''labels = GivenLabels("Car_Data.csv")
    for string in labels: 
        print(string + "\n")'''
    url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data")
    myData = pd.read_csv(url,header=None)
    #theData = data("Car_Data.csv")
    #train = trainingData("Car_Data.csv")
    print(myData)
    print("Data from the csv I created")
    #print(theData)
    #numbs = convertToNumbers(myData)
    '''for item in numbs:
        print(item.buying, end=" ")
        print(item.maint,end= " ")
        print(item.doors,end= " ")
        print(item.persons,end= " ")
        print(item.lugboat,end= " ")
        print(item.safety,end= " ")'''