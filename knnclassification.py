from Arrayify import *
import numpy as np
import random
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
class main:
    myData = data("Car_Data.csv")
    numbs = convertToNumbers(myData)
    labels = GivenLabels("Car_Data.csv")
    labels = replaceLabels(labels)
    train = trainingData(numbs)
    print(train)
    #np.random.shuffle(train)
    df = pd.DataFrame(train,columns=["buying","maint","doors","persons","luggage","safety"]) #dataframe
    print(df)
   
    correlationMatrix = df.corr() #correlation Matrix
    print(correlationMatrix["safety"])
    print(correlationMatrix["buying"])
    print(correlationMatrix["maint"])
    print(correlationMatrix["persons"])
    print(correlationMatrix["doors"])
    print(correlationMatrix["luggage"]) 
    df["class"] = labels
    plt.close()
    sns.set_style("whitegrid")
    sns.pairplot(df,hue="class",height=2) #scatterplot and classes
    plt.show()
    xData = df.drop(["class"],axis=1) #this uis for the data
    yData = df["class"]
    MinMaxScaler = preprocessing.MinMaxScaler()
    X_data_minmax = MinMaxScaler.fit_transform(xData)
    data = pd.DataFrame(X_data_minmax,columns=['buying', 'maint', 'doors', 'persons','luggage','safety'])
    df.head()
    X_train, X_test, y_train, y_test = train_test_split(data, yData,test_size=0.2, random_state = 1) #split data
    knn_clf=KNeighborsClassifier(n_neighbors=9) #run classifier and the best nearest neighbor for highest prediction
    knn_clf.fit(X_train,y_train) #fitting the training data
    ypred=knn_clf.predict(X_test) #predict
    result = confusion_matrix(y_test, ypred) #confusion matrix
    print("Confusion Matrix:")
    print(result)
    result1 = classification_report(y_test, ypred)
    print("Classification Report:")
    print (result1)
    result2 = accuracy_score(y_test,ypred) #setting accuracy
    print("Accuracy:",result2) #accuracy
    #print("This is the random dataset")
    #print(train) This was for testing on ways to get smaller accuracy
    #np.savetxt('Random_training_data.csv',train,delimiter=",")
    
