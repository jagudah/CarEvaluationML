import numpy as np
from numpy import genfromtxt
import pandas as pd
import csv
class Car:
    def __init__(self,buying,maint,doors,persons,lugboat,safety):
        self.buying = buying
        self.maint = maint
        self.doors = doors
        self.persons = persons
        self.lugboat = lugboat
        self.safety = safety

def data(file):
    myData = []
    with open(file,newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=' ',quotechar='|')
        for row in reader:
            for column in row:
                current = column.split(",")
                Car_Data = Car(current[0],current[1],current[2],current[3],current[4],current[5])
            myData.append(Car_Data)
    return myData 
