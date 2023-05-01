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
def replace4ranks(string):
    string = string.replace("vhigh","4")
    string = string.replace("high","3")
    string = string.replace("med","2")
    string = string.replace("low","1")
    return string

def replacePersons(string):
    string = string.replace("2", "1")
    string = string.replace("4", "2")
    string = string.replace("more", "3")
    return string

def replaceSize(string):
    string = string.replace("small", "1")
    string = string.replace("med", "2")
    string = string.replace("big", "3")
    return string

def replaceDoors(string):
    string = string.replace("2", "1")
    string = string.replace("3", "2")
    string = string.replace("4", "3")
    string = string.replace("5more","4")
    return string

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

def labels(file):
    labels = []
    with open(file,newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=' ',quotechar='|')
        for row in reader:
            for column in row:
                current = column.split(',')
                labels.append(current[6])
    return labels

def convertToNumbers(myData):
    #seatCount = {"2" : 1, "4" : 2 , "5more" : 3 }
    for row in myData:
            row.buying = int(replace4ranks(row.buying))
            row.maint = int(replace4ranks(row.maint))
            row.doors = int(replaceDoors(row.doors))
            row.persons = int(replacePersons(row.persons))
            row.lugboat = int(replaceSize(row.lugboat))
            row.safety = int(replace4ranks(row.safety))
    return myData