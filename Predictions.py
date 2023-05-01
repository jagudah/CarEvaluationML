from ClassificationTree import *
import sklearn
class main:
    fourRanks = ["vhigh","high","med","low"]
    numofPerson = ["2","4","more"]
    sizes = ["small","med","big"]
    doors = ["2","3","4","5more"]
    samples = []
    do_calulation = True
    print("Lets see if your car is acceptable \n Enter the following criteria\n")
    while(do_calulation):
        while True:
            cost = input("What is the cost of the Car? 1. vhigh 2. high 3. med 4. low\n")
            if cost in fourRanks:
                break
            else:
                print("Try again. This is not an option. enter the word exactly as seen\n")
        while True:
            maint = input("What is the maintenence cost of the Car? 1. vhigh 2. high 3. med 4. low\n")
            if maint in fourRanks:
                break
            else:
                print("Try again. This is not an option. enter the word exactly as seen\n")
        while True:
            amtofdoors = input("How many doors are in the car? 2 , 3 , 4 , 5more\n")
            if amtofdoors in doors:
                break
            else:
                print("Try again. This is not an option. enter the word exactly as seen\n")
        while True:
            persons = input("How many seats are in the Car? 2 ,4 , more\n")
            if persons in fourRanks:
                break
            else:
                print("Try again. This is not an option. enter the word exactly as seen\n")
        while True:
            luggage = input("What is the luggage size of the Car? 1. small 2. med 3. big\n ")
            if luggage in sizes:
                break
            else:
                print("Try again. This is not an option. enter the word exactly as seen\n")
        while True:
            safety = input("What is the safety of the Car? 1. low 2. med 3. high\n ")
            if safety in fourRanks:
                break
            else:
                print("Try again. This is not an option. enter the word exactly as seen\n")
        samples.append([int(replace4ranks(cost)),int(replace4ranks(maint)),int(replaceDoors(amtofdoors)),int(replacePersons(persons)),int(replaceSize(luggage)),int(replace4ranks(safety))])
        another_calculation = input("Do you want to perform another calculation? (y/n): ")
        if(another_calculation != "y"):
            do_calculation = False
            print(plt.predict(samples))