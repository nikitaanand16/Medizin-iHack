#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from  sklearn.metrics import confusion_matrix
#
def heart(i):
    dataset =pd.read_csv('static/heart.csv')
    X=dataset.iloc[:,0:8].values
    y=dataset.iloc[:,-1].values
    #
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.2,random_state=0)
    #
    from sklearn.preprocessing import StandardScaler
    sc_X= StandardScaler()
    #X_train=sc_X.fit_transform(X_train)
    #X_test=sc_X.fit_transform(X_test)
    #i=sc_X.fit_transform(i)
    #
    classifiers=[]

    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(random_state=0)
    classifier.fit(X_train,y_train)
    classifiers.append(classifier)

    from sklearn.neighbors import KNeighborsClassifier
    classifier = KNeighborsClassifier(n_neighbors=3,metric='minkowski',p=2)
    classifier.fit(X_train,y_train)
    classifiers.append(classifier)

    from sklearn.svm import SVC
    classifier = SVC(kernel ='linear', random_state=0)
    classifier.fit(X_train,y_train)
    classifiers.append(classifier)
        
    from sklearn.svm import SVC
    classifier = SVC(kernel ='poly', random_state=0)
    classifier.fit(X_train,y_train)
    classifiers.append(classifier)

    from sklearn.svm import SVC
    classifier = SVC(kernel ='sigmoid', random_state=0)
    classifier.fit(X_train,y_train)
    classifiers.append(classifier)

    from sklearn.svm import SVC
    classifier = SVC(kernel ='rbf', random_state=0)
    classifier.fit(X_train,y_train)
    classifiers.append(classifier)

    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier.fit(X_train,y_train)
    classifiers.append(classifier)
     
    from sklearn.tree import DecisionTreeClassifier
    classifier = DecisionTreeClassifier(criterion ='entropy',random_state=0)
    classifier.fit(X_train,y_train)
    classifiers.append(classifier)

    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators=20, criterion='entropy',random_state=0)
    classifier.fit(X_train,y_train)
    classifiers.append(classifier)
    #
    accuracy=[]
    precision=[]
    recall=[]
    f1_score=[]
    output=[]
    positive=0
    negative=0

    for classifier in classifiers:
        Y_pred = classifier.predict(X_test)
        z=classifier.predict(i)
        cm = confusion_matrix(y_test,Y_pred)
        a=(cm[0][0]+cm[1][1])*100/(cm[0][0]+cm[1][1]+cm[0][1]+cm[1][0])
        b=(cm[0][0])*100/(cm[0][0]+cm[1][0])
        c=(cm[0][0])*100/(cm[0][0]+cm[0][1])
        d=2*(c*b)/(c+b)
        a="{:.2f}".format(a)
        b="{:.2f}".format(b)
        c="{:.2f}".format(c)
        d="{:.2f}".format(d)
        accuracy.append(a)
        precision.append(b)
        recall.append(c)
        f1_score.append(d)

        if(z[0]==1):
            output+=["The patient will get heart disease"]
            positive+=1
        else:
            output+=["The patient will not get heart disease"]
            negative+=1
    f=positive+negative
    positive=(positive/f)*100
    negative=(negative/f)*100
    positive="{:.2f}".format(positive)
    negative="{:.2f}".format(negative)
    return accuracy,precision,recall,f1_score,output,positive,negative