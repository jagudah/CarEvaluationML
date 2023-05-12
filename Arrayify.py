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
#replace the attributes that rank vhigh-low into numbers
def replace4ranks(string):
    string = string.replace("vhigh","4")
    string = string.replace("high","3")
    string = string.replace("med","2")
    string = string.replace("low","1")
    return string
#replace the persons attribute into numbers
def replacePersons(string):
    string = string.replace("2", "1")
    string = string.replace("4", "2")
    string = string.replace("more", "3")
    return string
#replace size attribute into numbers
def replaceSize(string):
    string = string.replace("small", "1")
    string = string.replace("med", "2")
    string = string.replace("big", "3")
    return string
#replace doors attribute into numbers
def replaceDoors(string):
    string = string.replace("2", "1")
    string = string.replace("3", "2")
    string = string.replace("4", "3")
    string = string.replace("5more","4")
    return string
#make the labels/classes into numbers
def replaceLabels(labels):
    for string in labels:
        string = string.replace("unacc", "1")
        string = string.replace("acc", "2")
        string = string.replace("vgood","4")
        string = string.replace("good", "3")
        string = int(string)
    return labels
#Turns data file into array of objects
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
#Takes the last column of file and uses that as the labels
def GivenLabels(file):
    labels = []
    with open(file,newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=' ',quotechar='|')
        for row in reader:
            for column in row:
                current = column.split(',')
                labels.append(current[6])
    return labels
#This is for changing all of the words the data tells us into integers for classification
def convertToNumbers(myData):
    for row in myData:
            row.buying = int(replace4ranks(row.buying))
            row.maint = int(replace4ranks(row.maint))
            row.doors = int(replaceDoors(row.doors))
            row.persons = int(replacePersons(row.persons))
            row.lugboat = int(replaceSize(row.lugboat))
            row.safety = int(replace4ranks(row.safety))
    return myData

#This function turns the array of objects into a 2D array. Used for changing into a dataframe so the classifications can be easily run
def trainingData(myData):
    train = []
    for i in range(len(myData)):
        train.append([myData[i].buying,myData[i].maint,myData[i].doors,myData[i].persons,myData[i].lugboat,myData[i].safety])
    return train