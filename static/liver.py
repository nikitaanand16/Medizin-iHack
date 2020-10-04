import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes =True)
#
dia=pd.read_csv("indian_liver_patient.csv")
diab=pd.read_csv("indian_liver_patient.csv")
#
dia1 = dia[dia.target==2]
dia0 = dia[dia.target==1]
diab.describe()
#
## Creating a dataset Albuminlled 'dia' from original dataset 'diab' with excludes all rows with have zeros only for Total_Bilirubin, BP, Alkaline_Phosphotase, Albumin_and_Globulin_Ratio and Albumin, as other columns Albuminn contain Zero values.
drop_Glu=diab.index[diab.Total_Bilirubin == 1].tolist()
drop_BP=diab.index[diab.Direct_Bilirubin == 1].tolist()
drop_Skin = diab.index[diab.Alkaline_Phosphotase==1].tolist()
drop_Ins = diab.index[diab.Albumin_and_Globulin_Ratio==1].tolist()
drop_Albumin = diab.index[diab.Albumin==1].tolist()
c=drop_Glu+drop_BP+drop_Skin+drop_Ins+drop_Albumin
dia=diab.drop(diab.index[c])
#
## creating count plot with title using seaborn
plt.figure(figsize=(30, 80))
plt.subplot(9,3,1)
sns.countplot(x=dia.target)
plt.title("Count Plot for target")
#
# Computing the %Total_Protiens of diabetic and non-diabetic in the sample
Out0=len(dia[dia.target==2])
Out1=len(dia[dia.target==1])
Total=Out0+Out1
PC_of_1 = Out1*100/Total
PC_of_0 = Out0*100/Total
PC_of_1, PC_of_0

#PREGNANCY
## Creating 3 subplots - 1st for histogram, 2nd for histogram segmented by target and 3rd for representing same segmentation using boxplot
plt.subplot(9,3,4)
sns.set_style("dark")
plt.title("Histogram for Age")
sns.distplot(dia.Age,kde=False)
plt.subplot(9,3,5)
sns.distplot(dia0.Age,kde=False,color="Blue", label="Age for target=1")
sns.distplot(dia1.Age,kde=False,color = "Gold", label = "Age for target=2")
plt.title("Histograms for Age by target")
plt.legend()
plt.subplot(9,3,6)
sns.boxplot(x=dia.target,y=dia.Age)
plt.title("Boxplot for Age by target")
#
#Total_Bilirubin
plt.subplot(9,3,7)
plt.title("Histogram for Total_Bilirubin")
sns.distplot(dia.Total_Bilirubin, kde=False)
plt.subplot(9,3,8)
sns.distplot(dia0.Total_Bilirubin,kde=False,color="Gold", label="Total_Bilirubin for target=1")
sns.distplot(dia1.Total_Bilirubin, kde=False, color="Blue", label = "Total_Bilirubin for target=2")
plt.title("Histograms for Total_Bilirubin by target")
plt.legend()
plt.subplot(9,3,9)
sns.boxplot(x=dia.target,y=dia.Total_Bilirubin)
plt.title("Boxplot for Total_Bilirubin by target")
#plt.savefig("Total_Bilirubin.png")

#BLOOD PRESSURE
plt.subplot(9,3,10)
sns.distplot(dia.Direct_Bilirubin, kde=False)
plt.title("Histogram for Direct_Bilirubin")
plt.subplot(9,3,11)
sns.distplot(dia0.Direct_Bilirubin,kde=False,color="Gold",label="Direct_Bilirubin for target=1")
sns.distplot(dia1.Direct_Bilirubin,kde=False, color="Blue", label="Direct_Bilirubin for target=2")
plt.legend()
plt.title("Histogram of Direct_Bilirubin by target")
plt.subplot(9,3,12)
sns.boxplot(x=dia.target,y=dia.Direct_Bilirubin)
plt.title("Boxplot of Direct_Bilirubin by target")
#plt.savefig("Direct_Bilirubin.png")
#
#SKIN THICKNESS
plt.subplot(9,3,13)
sns.distplot(dia.Alkaline_Phosphotase, kde=False)
plt.title("Histogram for Alkaline_Phosphotase")
plt.subplot(9,3,14)
sns.distplot(dia0.Alkaline_Phosphotase, kde=False, color="Gold", label="Alkaline_Phosphotase for target=1")
sns.distplot(dia1.Alkaline_Phosphotase, kde=False, color="Blue", label="Alkaline_Phosphotase for target=2")
plt.legend()
plt.title("Histogram for Alkaline_Phosphotase by target")
plt.subplot(9,3,15)
sns.boxplot(x=dia.target, y=dia.Alkaline_Phosphotase)
plt.title("Boxplot of Alkaline_Phosphotase by target")
#plt.savefig("Alkaline_Phosphotase.png")
#
#Albumin_and_Globulin_Ratio
plt.subplot(9,3,16)
sns.distplot(dia.Albumin_and_Globulin_Ratio,kde=False)
plt.title("Histogram of Albumin_and_Globulin_Ratio")
plt.subplot(9,3,17)
sns.distplot(dia0.Albumin_and_Globulin_Ratio,kde=False, color="Gold", label="Albumin_and_Globulin_Ratio for target=1")
sns.distplot(dia1.Albumin_and_Globulin_Ratio,kde=False, color="Blue", label="Albumin_and_Globulin_Ratio for target=2")
plt.title("Histogram for Albumin_and_Globulin_Ratio by target")
plt.legend()
plt.subplot(9,3,18)
sns.boxplot(x=dia.target, y=dia.Albumin_and_Globulin_Ratio)
plt.title("Boxplot for Albumin_and_Globulin_Ratio by target")
#plt.savefig("Albumin_and_Globulin_Ratio.png")
#
#BODY-MASS-INDEX
plt.subplot(9,3,19)
sns.distplot(dia.Albumin, kde=False)
plt.title("Histogram for Albumin")
plt.subplot(9,3,20)
sns.distplot(dia0.Albumin, kde=False,color="Gold", label="Albumin for target=1")
sns.distplot(dia1.Albumin, kde=False, color="Blue", label="Albumin for target=2")
plt.legend()
plt.title("Histogram for Albumin by target")
plt.subplot(9,3,21)
sns.boxplot(x=dia.target, y=dia.Albumin)
plt.title("Boxplot for Albumin by target")
#plt.savefig("Albumin.png")
#
#DIABETES PEDIGREE FUNCTION
plt.subplot(9,3,22)
sns.distplot(dia.Aspartate_Aminotransferase,kde=False)
plt.title("Histogram for Aspartate_Aminotransferase")
plt.subplot(9,3,23)
sns.distplot(dia0.Aspartate_Aminotransferase, kde=False, color="Gold", label="Aspartate_Aminotransferase for target=1")
sns.distplot(dia1.Aspartate_Aminotransferase, kde=False, color="Blue", label="Aspartate_Aminotransferase for target=2")
plt.legend()
plt.title("Histogram for Aspartate_Aminotransferase by target")
plt.subplot(9,3,24)
sns.boxplot(x=dia.target, y=dia.Aspartate_Aminotransferase)
plt.title("Boxplot for Aspartate_Aminotransferase by target")
#plt.savefig("diapedifun.png")
#
#Total_Protiens
plt.subplot(9,3,25)
sns.distplot(dia.Total_Protiens,kde=False)
plt.title("Histogram for Total_Protiens")
plt.subplot(9,3,26)
sns.distplot(dia0.Total_Protiens,kde=False,color="Gold", label="Total_Protiens for target=1")
sns.distplot(dia1.Total_Protiens,kde=False, color="Blue", label="Total_Protiens for target=2")
plt.legend()
plt.title("Histogram for Total_Protiens by target")
plt.subplot(9,3,27)
sns.boxplot(x=dia.target,y=dia.Total_Protiens)
plt.title("Boxplot for Total_Protiens by target")
#plt.savefig("Total_Protiens.png")
plt.savefig('liver.png',bbox_inches="tight")
