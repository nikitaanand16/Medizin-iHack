import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes =True)
#
dia=pd.read_csv("lung_cancer_examples.csv")
diab=pd.read_csv("lung_cancer_examples.csv")
#
dia1 = dia[dia.Result==1]
dia0 = dia[dia.Result==0]
diab.describe()
#
## Creating a dataset called 'dia' from original dataset 'diab' with excludes all rows with have zeros only for Age, BP, AreaQ, Alkhol and BMI, as other columns can contain Zero values.
drop_Glu=diab.index[diab.Age == 0].tolist()
drop_BP=diab.index[diab.Smokes == 0].tolist()
drop_Skin = diab.index[diab.AreaQ==0].tolist()
drop_Ins = diab.index[diab.Alkhol==0].tolist()
c=drop_Glu+drop_BP+drop_Skin+drop_Ins
dia=diab.drop(diab.index[c])
#
## creating count plot with title using seaborn
plt.figure(figsize=(30, 45))
plt.subplot(5,3,1)
sns.countplot(x=dia.Result)
plt.title("Count Plot for Result")
#
# Computing the %age of diabetic and non-diabetic in the sample
Out0=len(dia[dia.Result==1])
Out1=len(dia[dia.Result==0])
Total=Out0+Out1
PC_of_1 = Out1*100/Total
PC_of_0 = Out0*100/Total
PC_of_1, PC_of_0


## Creating 3 subplots - 1st for histogram, 2nd for histogram segmented by Result and 3rd for representing same segmentation using boxplot
#
#Age
plt.subplot(5,3,4)
plt.title("Histogram for Age")
sns.distplot(dia.Age, kde=False)
plt.subplot(5,3,5)
sns.distplot(dia0.Age,kde=False,color="Gold", label="Age for Result=0")
sns.distplot(dia1.Age, kde=False, color="Blue", label = "Age for Result=1")
plt.title("Histograms for Age by Result")
plt.legend()
plt.subplot(5,3,6)
sns.boxplot(x=dia.Result,y=dia.Age)
plt.title("Boxplot for Age by Result")
#plt.savefig("Age.png")

#BLOOD PRESSURE
plt.subplot(5,3,7)
sns.distplot(dia.Smokes, kde=False)
plt.title("Histogram for Smokes")
plt.subplot(5,3,8)
sns.distplot(dia0.Smokes,kde=False,color="Gold",label="Smokes for Result=0")
sns.distplot(dia1.Smokes,kde=False, color="Blue", label="Smokes for Result=1")
plt.legend()
plt.title("Histogram of Smokes by Result")
plt.subplot(5,3,9)
sns.boxplot(x=dia.Result,y=dia.Smokes)
plt.title("Boxplot of Smokes by Result")
#plt.savefig("Smokes.png")
#
#SKIN THICKNESS
plt.subplot(5,3,10)
sns.distplot(dia.AreaQ, kde=False)
plt.title("Histogram for AreaQ")
plt.subplot(5,3,11)
sns.distplot(dia0.AreaQ, kde=False, color="Gold", label="AreaQ for Result=0")
sns.distplot(dia1.AreaQ, kde=False, color="Blue", label="AreaQ for Result=1")
plt.legend()
plt.title("Histogram for AreaQ by Result")
plt.subplot(5,3,12)
sns.boxplot(x=dia.Result, y=dia.AreaQ)
plt.title("Boxplot of AreaQ by Result")
#plt.savefig("AreaQ.png")
#
#Alkhol
plt.subplot(5,3,13)
sns.distplot(dia.Alkhol,kde=False)
plt.title("Histogram of Alkhol")
plt.subplot(5,3,14)
sns.distplot(dia0.Alkhol,kde=False, color="Gold", label="Alkhol for Result=0")
sns.distplot(dia1.Alkhol,kde=False, color="Blue", label="Alkhol for Result=1")
plt.title("Histogram for Alkhol by Result")
plt.legend()
plt.subplot(5,3,15)
sns.boxplot(x=dia.Result, y=dia.Alkhol)
plt.title("Boxplot for Alkhol by Result")
#plt.savefig("Alkhol.png")
#

plt.savefig('lung.png',bbox_inches="tight")
