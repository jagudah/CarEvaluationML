import numpy as np
from numpy import genfromtxt
import pandas as pd
import csv
def data(file):
    myData = []
    with open(file,newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=' ',quotechar='|')
        for row in reader:
            myData.append(row)
    return myData 
