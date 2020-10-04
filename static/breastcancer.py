import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def graph():
	sns.set(color_codes =True)
	#
	dia=pd.read_csv("static/breastcancer.csv")
	diab=pd.read_csv("static/breastcancer.csv")
	#
	dia1 = dia[dia.diagnosis=='M']
	dia0 = dia[dia.diagnosis=='B']
	diab.describe()
	#
	## Creating a dataset compactness_meanlled 'dia' from original dataset 'diab' with excludes all rows with have zeros only for area_mean, BP, radius_mean, texture_mean and compactness_mean, as other columns compactness_meann contain Zero values.
	drop_Glu=diab.index[diab.area_mean == 'B'].tolist()
	drop_BP=diab.index[diab.perimeter_mean == 'B'].tolist()
	drop_Skin = diab.index[diab.radius_mean=='B'].tolist()
	drop_Ins = diab.index[diab.texture_mean=='B'].tolist()
	drop_compactness_mean = diab.index[diab.compactness_mean=='B'].tolist()
	c=drop_Glu+drop_BP+drop_Skin+drop_Ins+drop_compactness_mean
	dia=diab.drop(diab.index[c])
	#
	## creating count plot with title using seaborn
	plt.figure(figsize=(30, 80))
	plt.subplot(9,3,1)
	sns.countplot(x=dia.diagnosis)
	plt.title("Count Plot for diagnosis")
	#
	# Computing the %concavity_mean of diabetic and non-diabetic in the sample
	Out0=len(dia[dia.diagnosis=='M'])
	Out1=len(dia[dia.diagnosis=='B'])
	Total=Out0+Out1
	PC_of_1 = Out1*100/Total
	PC_of_0 = Out0*100/Total
	PC_of_1, PC_of_0

	#PREGNANCY
	## Creating 3 subplots - 1st for histogram, 2nd for histogram segmented by diagnosis and 3rd for representing same segmentation using boxplot
	plt.subplot(9,3,4)
	sns.set_style("dark")
	plt.title("Histogram for smoothness_mean")
	sns.distplot(dia.smoothness_mean,kde=False)
	plt.subplot(9,3,5)
	sns.distplot(dia0.smoothness_mean,kde=False,color="Blue", label="smoothness_mean for Outome=0")
	sns.distplot(dia1.smoothness_mean,kde=False,color = "Gold", label = "smoothness_mean for diagnosis=1")
	plt.title("Histograms for smoothness_mean by diagnosis")
	plt.legend()
	plt.subplot(9,3,6)
	sns.boxplot(x=dia.diagnosis,y=dia.smoothness_mean)
	plt.title("Boxplot for smoothness_mean by diagnosis")
	#
	#area_mean
	plt.subplot(9,3,7)
	plt.title("Histogram for area_mean")
	sns.distplot(dia.area_mean, kde=False)
	plt.subplot(9,3,8)
	sns.distplot(dia0.area_mean,kde=False,color="Gold", label="area_mean for diagnosis=0")
	sns.distplot(dia1.area_mean, kde=False, color="Blue", label = "area_mean for diagnosis=1")
	plt.title("Histograms for area_mean by diagnosis")
	plt.legend()
	plt.subplot(9,3,9)
	sns.boxplot(x=dia.diagnosis,y=dia.area_mean)
	plt.title("Boxplot for area_mean by diagnosis")
	#plt.savefig("area_mean.png")

	#BLOOD PRESSURE
	plt.subplot(9,3,10)
	sns.distplot(dia.perimeter_mean, kde=False)
	plt.title("Histogram for perimeter_mean")
	plt.subplot(9,3,11)
	sns.distplot(dia0.perimeter_mean,kde=False,color="Gold",label="perimeter_mean for diagnosis=0")
	sns.distplot(dia1.perimeter_mean,kde=False, color="Blue", label="perimeter_mean for diagnosis=1")
	plt.legend()
	plt.title("Histogram of perimeter_mean by diagnosis")
	plt.subplot(9,3,12)
	sns.boxplot(x=dia.diagnosis,y=dia.perimeter_mean)
	plt.title("Boxplot of perimeter_mean by diagnosis")
	#plt.savefig("perimeter_mean.png")
	#
	#SKIN THICKNESS
	plt.subplot(9,3,13)
	sns.distplot(dia.radius_mean, kde=False)
	plt.title("Histogram for radius_mean")
	plt.subplot(9,3,14)
	sns.distplot(dia0.radius_mean, kde=False, color="Gold", label="radius_mean for diagnosis=0")
	sns.distplot(dia1.radius_mean, kde=False, color="Blue", label="radius_mean for diagnosis=1")
	plt.legend()
	plt.title("Histogram for radius_mean by diagnosis")
	plt.subplot(9,3,15)
	sns.boxplot(x=dia.diagnosis, y=dia.radius_mean)
	plt.title("Boxplot of radius_mean by diagnosis")
	#plt.savefig("radius_mean.png")
	#
	#texture_mean
	plt.subplot(9,3,16)
	sns.distplot(dia.texture_mean,kde=False)
	plt.title("Histogram of texture_mean")
	plt.subplot(9,3,17)
	sns.distplot(dia0.texture_mean,kde=False, color="Gold", label="texture_mean for diagnosis=0")
	sns.distplot(dia1.texture_mean,kde=False, color="Blue", label="texture_mean for diagnosis=1")
	plt.title("Histogram for texture_mean by diagnosis")
	plt.legend()
	plt.subplot(9,3,18)
	sns.boxplot(x=dia.diagnosis, y=dia.texture_mean)
	plt.title("Boxplot for texture_mean by diagnosis")
	#plt.savefig("texture_mean.png")
	#
	#BODY-MASS-INDEX
	plt.subplot(9,3,19)
	sns.distplot(dia.compactness_mean, kde=False)
	plt.title("Histogram for compactness_mean")
	plt.subplot(9,3,20)
	sns.distplot(dia0.compactness_mean, kde=False,color="Gold", label="compactness_mean for diagnosis=0")
	sns.distplot(dia1.compactness_mean, kde=False, color="Blue", label="compactness_mean for diagnosis=1")
	plt.legend()
	plt.title("Histogram for compactness_mean by diagnosis")
	plt.subplot(9,3,21)
	sns.boxplot(x=dia.diagnosis, y=dia.compactness_mean)
	plt.title("Boxplot for compactness_mean by diagnosis")
	#plt.savefig("compactness_mean.png")
	#
	#DIABETES PEDIGREE FUNCTION
	plt.subplot(9,3,22)
	sns.distplot(dia.symmetry_mean,kde=False)
	plt.title("Histogram for symmetry_mean")
	plt.subplot(9,3,23)
	sns.distplot(dia0.symmetry_mean, kde=False, color="Gold", label="symmetry_mean for diagnosis=0")
	sns.distplot(dia1.symmetry_mean, kde=False, color="Blue", label="symmetry_mean for diagnosis=1")
	plt.legend()
	plt.title("Histogram for symmetry_mean by diagnosis")
	plt.subplot(9,3,24)
	sns.boxplot(x=dia.diagnosis, y=dia.symmetry_mean)
	plt.title("Boxplot for symmetry_mean by diagnosis")
	#plt.savefig("diapedifun.png")
	#
	#concavity_mean
	plt.subplot(9,3,25)
	sns.distplot(dia.concavity_mean,kde=False)
	plt.title("Histogram for concavity_mean")
	plt.subplot(9,3,26)
	sns.distplot(dia0.concavity_mean,kde=False,color="Gold", label="concavity_mean for diagnosis=0")
	sns.distplot(dia1.concavity_mean,kde=False, color="Blue", label="concavity_mean for diagnosis=1")
	plt.legend()
	plt.title("Histogram for concavity_mean by diagnosis")
	plt.subplot(9,3,27)
	sns.boxplot(x=dia.diagnosis,y=dia.concavity_mean)
	plt.title("Boxplot for concavity_mean by diagnosis")
	#plt.savefig("concavity_mean.png")
	plt.savefig('static/test.png',bbox_inches="tight")
	#plt.close()
