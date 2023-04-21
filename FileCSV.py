import pandas
dataframe = pandas.read_csv("Car_Data.txt",delimiter=",")
dataframe.to_csv("Car_Data.csv",index=None)