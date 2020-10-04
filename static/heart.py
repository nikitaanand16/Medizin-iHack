import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def heartvisual():
    sns.set(color_codes =True)
#
    dia=pd.read_csv("static/heart.csv")
    diab=pd.read_csv("static/heart.csv")
    #
    dia1 = dia[dia.target==1]
    dia0 = dia[dia.target==0]
    diab.describe()
    #
    ## Creating a dataset oldpeaklled 'dia' from original dataset 'diab' with excludes all rows with have zeros only for trestbps, BP, thalach, ca and oldpeak, as other columns oldpeakn contain Zero values.
    drop_Glu=diab.index[diab.trestbps == 0].tolist()
    drop_BP=diab.index[diab.chol == 0].tolist()
    drop_Skin = diab.index[diab.thalach==0].tolist()
    drop_Ins = diab.index[diab.ca==0].tolist()
    drop_oldpeak = diab.index[diab.oldpeak==0].tolist()
    c=drop_Glu+drop_BP+drop_Skin+drop_Ins+drop_oldpeak
    dia=diab.drop(diab.index[c])
    #
    ## creating count plot with title using seaborn
    plt.figure(figsize=(30, 80))
    plt.subplot(9,3,1)
    sns.countplot(x=dia.target)
    plt.title("Count Plot for target")
    #
    # Computing the %age of diabetic and non-diabetic in the sample
    Out0=len(dia[dia.target==1])
    Out1=len(dia[dia.target==0])
    Total=Out0+Out1
    PC_of_1 = Out1*100/Total
    PC_of_0 = Out0*100/Total
    PC_of_1, PC_of_0
    
    #PREGNANCY
    ## Creating 3 subplots - 1st for histogram, 2nd for histogram segmented by target and 3rd for representing same segmentation using boxplot
    plt.subplot(9,3,4)
    sns.set_style("dark")
    plt.title("Histogram for cp")
    sns.distplot(dia.cp,kde=False)
    plt.subplot(9,3,5)
    sns.distplot(dia0.cp,kde=False,color="Blue", label="cp for target=0")
    sns.distplot(dia1.cp,kde=False,color = "Gold", label = "cp for target=1")
    plt.title("Histograms for cp by target")
    plt.legend()
    plt.subplot(9,3,6)
    sns.boxplot(x=dia.target,y=dia.cp)
    plt.title("Boxplot for cp by target")
    #
    #trestbps
    plt.subplot(9,3,7)
    plt.title("Histogram for trestbps")
    sns.distplot(dia.trestbps, kde=False)
    plt.subplot(9,3,8)
    sns.distplot(dia0.trestbps,kde=False,color="Gold", label="trestbps for target=0")
    sns.distplot(dia1.trestbps, kde=False, color="Blue", label = "trestbps for target=1")
    plt.title("Histograms for trestbps by target")
    plt.legend()
    plt.subplot(9,3,9)
    sns.boxplot(x=dia.target,y=dia.trestbps)
    plt.title("Boxplot for trestbps by target")
    #plt.savefig("trestbps.png")
    
    #BLOOD PRESSURE
    plt.subplot(9,3,10)
    sns.distplot(dia.chol, kde=False)
    plt.title("Histogram for chol")
    plt.subplot(9,3,11)
    sns.distplot(dia0.chol,kde=False,color="Gold",label="chol for target=0")
    sns.distplot(dia1.chol,kde=False, color="Blue", label="chol for target=1")
    plt.legend()
    plt.title("Histogram of chol by target")
    plt.subplot(9,3,12)
    sns.boxplot(x=dia.target,y=dia.chol)
    plt.title("Boxplot of chol by target")
    #plt.savefig("chol.png")
    #
    #SKIN THICKNESS
    plt.subplot(9,3,13)
    sns.distplot(dia.thalach, kde=False)
    plt.title("Histogram for thalach")
    plt.subplot(9,3,14)
    sns.distplot(dia0.thalach, kde=False, color="Gold", label="thalach for target=0")
    sns.distplot(dia1.thalach, kde=False, color="Blue", label="thalach for target=1")
    plt.legend()
    plt.title("Histogram for thalach by target")
    plt.subplot(9,3,15)
    sns.boxplot(x=dia.target, y=dia.thalach)
    plt.title("Boxplot of thalach by target")
    #plt.savefig("thalach.png")
    #
    #ca
    plt.subplot(9,3,16)
    sns.distplot(dia.ca,kde=False)
    plt.title("Histogram of ca")
    plt.subplot(9,3,17)
    sns.distplot(dia0.ca,kde=False, color="Gold", label="ca for target=0")
    sns.distplot(dia1.ca,kde=False, color="Blue", label="ca for target=1")
    plt.title("Histogram for ca by target")
    plt.legend()
    plt.subplot(9,3,18)
    sns.boxplot(x=dia.target, y=dia.ca)
    plt.title("Boxplot for ca by target")
    #plt.savefig("ca.png")
    #
    #BODY-MASS-INDEX
    plt.subplot(9,3,19)
    sns.distplot(dia.oldpeak, kde=False)
    plt.title("Histogram for oldpeak")
    plt.subplot(9,3,20)
    sns.distplot(dia0.oldpeak, kde=False,color="Gold", label="oldpeak for target=0")
    sns.distplot(dia1.oldpeak, kde=False, color="Blue", label="oldpeak for target=1")
    plt.legend()
    plt.title("Histogram for oldpeak by target")
    plt.subplot(9,3,21)
    sns.boxplot(x=dia.target, y=dia.oldpeak)
    plt.title("Boxplot for oldpeak by target")
    #plt.savefig("oldpeak.png")
    #
    #DIABETES PEDIGREE FUNCTION
    plt.subplot(9,3,22)
    sns.distplot(dia.restecg,kde=False)
    plt.title("Histogram for restecg")
    plt.subplot(9,3,23)
    sns.distplot(dia0.restecg, kde=False, color="Gold", label="restecg for target=0")
    sns.distplot(dia1.restecg, kde=False, color="Blue", label="restecg for target=1")
    plt.legend()
    plt.title("Histogram for restecg by target")
    plt.subplot(9,3,24)
    sns.boxplot(x=dia.target, y=dia.restecg)
    plt.title("Boxplot for restecg by target")
    #plt.savefig("diapedifun.png")
    #
    #age
    plt.subplot(9,3,25)
    sns.distplot(dia.age,kde=False)
    plt.title("Histogram for age")
    plt.subplot(9,3,26)
    sns.distplot(dia0.age,kde=False,color="Gold", label="age for target=0")
    sns.distplot(dia1.age,kde=False, color="Blue", label="age for target=1")
    plt.legend()
    plt.title("Histogram for age by target")
    plt.subplot(9,3,27)
    sns.boxplot(x=dia.target,y=dia.age)
    plt.title("Boxplot for age by target")
    #plt.savefig("age.png")
    plt.savefig('static/test.png',bbox_inches="tight")
    #plt.close()
    

