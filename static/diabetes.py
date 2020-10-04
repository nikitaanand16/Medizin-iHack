import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def make():
	sns.set(color_codes =True)
#
	dia=pd.read_csv("static/diabetes.csv")
	diab=pd.read_csv("static/diabetes.csv")
	#
	dia1 = dia[dia.Outcome==1]
	dia0 = dia[dia.Outcome==0]
	diab.describe()
	#
	## Creating a dataset called 'dia' from original dataset 'diab' with excludes all rows with have zeros only for Glucose, BP, Skinthickness, Insulin and BMI, as other columns can contain Zero values.
	drop_Glu=diab.index[diab.Glucose == 0].tolist()
	drop_BP=diab.index[diab.BloodPressure == 0].tolist()
	drop_Skin = diab.index[diab.SkinThickness==0].tolist()
	drop_Ins = diab.index[diab.Insulin==0].tolist()
	drop_BMI = diab.index[diab.BMI==0].tolist()
	c=drop_Glu+drop_BP+drop_Skin+drop_Ins+drop_BMI
	dia=diab.drop(diab.index[c])
	#
	## creating count plot with title using seaborn
	plt.figure(figsize=(30, 80))
	plt.subplot(9,3,1)
	sns.countplot(x=dia.Outcome)
	plt.title("Count Plot for Outcome")
	#
	# Computing the %age of diabetic and non-diabetic in the sample
	Out0=len(dia[dia.Outcome==1])
	Out1=len(dia[dia.Outcome==0])
	Total=Out0+Out1
	PC_of_1 = Out1*100/Total
	PC_of_0 = Out0*100/Total
	PC_of_1, PC_of_0

	#PREGNANCY
	## Creating 3 subplots - 1st for histogram, 2nd for histogram segmented by Outcome and 3rd for representing same segmentation using boxplot
	plt.subplot(9,3,4)
	sns.set_style("dark")
	plt.title("Histogram for Pregnancies")
	sns.distplot(dia.Pregnancies,kde=False)
	plt.subplot(9,3,5)
	sns.distplot(dia0.Pregnancies,kde=False,color="Blue", label="Preg for Outome=0")
	sns.distplot(dia1.Pregnancies,kde=False,color = "Gold", label = "Preg for Outcome=1")
	plt.title("Histograms for Preg by Outcome")
	plt.legend()
	plt.subplot(9,3,6)
	sns.boxplot(x=dia.Outcome,y=dia.Pregnancies)
	plt.title("Boxplot for Preg by Outcome")
	#
	#GLUCOSE
	plt.subplot(9,3,7)
	plt.title("Histogram for Glucose")
	sns.distplot(dia.Glucose, kde=False)
	plt.subplot(9,3,8)
	sns.distplot(dia0.Glucose,kde=False,color="Gold", label="Gluc for Outcome=0")
	sns.distplot(dia1.Glucose, kde=False, color="Blue", label = "Gloc for Outcome=1")
	plt.title("Histograms for Glucose by Outcome")
	plt.legend()
	plt.subplot(9,3,9)
	sns.boxplot(x=dia.Outcome,y=dia.Glucose)
	plt.title("Boxplot for Glucose by Outcome")
	#plt.savefig("glucose.png")

	#BLOOD PRESSURE
	plt.subplot(9,3,10)
	sns.distplot(dia.BloodPressure, kde=False)
	plt.title("Histogram for Blood Pressure")
	plt.subplot(9,3,11)
	sns.distplot(dia0.BloodPressure,kde=False,color="Gold",label="BP for Outcome=0")
	sns.distplot(dia1.BloodPressure,kde=False, color="Blue", label="BP for Outcome=1")
	plt.legend()
	plt.title("Histogram of Blood Pressure by Outcome")
	plt.subplot(9,3,12)
	sns.boxplot(x=dia.Outcome,y=dia.BloodPressure)
	plt.title("Boxplot of BP by Outcome")
	#plt.savefig("bloodpressure.png")
	#
	#SKIN THICKNESS
	plt.subplot(9,3,13)
	sns.distplot(dia.SkinThickness, kde=False)
	plt.title("Histogram for Skin Thickness")
	plt.subplot(9,3,14)
	sns.distplot(dia0.SkinThickness, kde=False, color="Gold", label="SkinThick for Outcome=0")
	sns.distplot(dia1.SkinThickness, kde=False, color="Blue", label="SkinThick for Outcome=1")
	plt.legend()
	plt.title("Histogram for SkinThickness by Outcome")
	plt.subplot(9,3,15)
	sns.boxplot(x=dia.Outcome, y=dia.SkinThickness)
	plt.title("Boxplot of SkinThickness by Outcome")
	#plt.savefig("skinthickness.png")
	#
	#INSULIN
	plt.subplot(9,3,16)
	sns.distplot(dia.Insulin,kde=False)
	plt.title("Histogram of Insulin")
	plt.subplot(9,3,17)
	sns.distplot(dia0.Insulin,kde=False, color="Gold", label="Insulin for Outcome=0")
	sns.distplot(dia1.Insulin,kde=False, color="Blue", label="Insuline for Outcome=1")
	plt.title("Histogram for Insulin by Outcome")
	plt.legend()
	plt.subplot(9,3,18)
	sns.boxplot(x=dia.Outcome, y=dia.Insulin)
	plt.title("Boxplot for Insulin by Outcome")
	#plt.savefig("insulin.png")
	#
	#BODY-MASS-INDEX
	plt.subplot(9,3,19)
	sns.distplot(dia.BMI, kde=False)
	plt.title("Histogram for BMI")
	plt.subplot(9,3,20)
	sns.distplot(dia0.BMI, kde=False,color="Gold", label="BMI for Outcome=0")
	sns.distplot(dia1.BMI, kde=False, color="Blue", label="BMI for Outcome=1")
	plt.legend()
	plt.title("Histogram for BMI by Outcome")
	plt.subplot(9,3,21)
	sns.boxplot(x=dia.Outcome, y=dia.BMI)
	plt.title("Boxplot for BMI by Outcome")
	#plt.savefig("BMI.png")
	#
	#DIABETES PEDIGREE FUNCTION
	plt.subplot(9,3,22)
	sns.distplot(dia.DiabetesPedigreeFunction,kde=False)
	plt.title("Histogram for Diabetes Pedigree Function")
	plt.subplot(9,3,23)
	sns.distplot(dia0.DiabetesPedigreeFunction, kde=False, color="Gold", label="PedFunction for Outcome=0")
	sns.distplot(dia1.DiabetesPedigreeFunction, kde=False, color="Blue", label="PedFunction for Outcome=1")
	plt.legend()
	plt.title("Histogram for DiabetesPedigreeFunction by Outcome")
	plt.subplot(9,3,24)
	sns.boxplot(x=dia.Outcome, y=dia.DiabetesPedigreeFunction)
	plt.title("Boxplot for DiabetesPedigreeFunction by Outcome")
	#plt.savefig("diapedifun.png")
	#
	#AGE
	plt.subplot(9,3,25)
	sns.distplot(dia.Age,kde=False)
	plt.title("Histogram for Age")
	plt.subplot(9,3,26)
	sns.distplot(dia0.Age,kde=False,color="Gold", label="Age for Outcome=0")
	sns.distplot(dia1.Age,kde=False, color="Blue", label="Age for Outcome=1")
	plt.legend()
	plt.title("Histogram for Age by Outcome")
	plt.subplot(9,3,27)
	sns.boxplot(x=dia.Outcome,y=dia.Age)
	plt.title("Boxplot for Age by Outcome")
	#plt.savefig("age.png")
	plt.savefig('static/test.png',bbox_inches="tight")
	#plt.close()

