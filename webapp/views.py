from django.shortcuts import render,redirect
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from static.diabetes import make
from static.diapredict import check
from static.breastcancer import graph
from static.tumortype import tumors
from webapp.models import Doctors,Questions,Answers
import time
from static.heart import heartvisual
from static.heartpredict import heart



# Create your views here
def index(request):
	return render(request,'start.html')

def expert(request):
	return render(request,'homepage.html')

def reply(request):
	answer=Answers.objects.all()[::-1]
	return render(request,'reply.html',{'answer' : answer})

def search(request):
	a=str(request.POST.get('find'))
	answer=Answers.objects.filter(patientnumber=a)
	return render(request,'reply.html',{'answer' : answer})

def doc(request):
	doctor=Doctors.objects.all()
	return render(request,'viewdoctors.html',{'doctor' : doctor})

def patientq(request):
	if(request.method=='POST'):
		global x
		x=str(request.POST.get("subject"))
		return render(request,'patienta.html')
	else:
		j=False
		question=Questions.objects.all()
		return render(request,'patientq.html',{'question' : question,'j':j})

def patienta(request):
	j=False
	if(request.method=='POST'):
		j=True
		a=request.POST.get('Name')
		b=request.POST.get('Hospital')
		c=request.POST.get('Phone')
		#d=request.POST.get('question')
		e=request.POST.get('solution')
		f=request.POST.get('medicine')
		global x
		question=Questions.objects.filter(Problem=x)
		y=question.values('Name')
		z=question.values('Phone')
		answer=Answers()
		answer.Name = a
		answer.Hospital = b
		answer.Phone = c
		answer.patientname=y
		answer.patientnumber=z
		answer.Problem= x
		answer.Answer= e
		answer.Medicine= f
		answer.save()
		Questions.objects.filter(Problem=x).delete()
		question=Questions.objects.all()
		return render(request,'patientq.html',{'question' : question, 'j':j})
	else:
		return render(request,'patienta.html')

def add(request):
	j=False
	if(request.method=='POST'):
		a=request.POST.get('Name')
		b=request.POST.get('Age')
		c=request.POST.get('Qualifications')
		d=request.POST.get('Years of Experience')
		e=request.POST.get('Gender')
		f=request.POST.get('Specialization')
		g=request.POST.get('Hospital')
		h=request.POST.get('Phone number')
		i=request.POST.get('Email')
		j=request.POST.get('from')
		k=request.POST.get('till')
		l=request.POST.get('Hospital Address')
		doctor=Doctors()
		doctor.Name = a
		doctor.Age = b
		doctor.Qualification = c
		doctor.Experience = d
		doctor.Gender = e
		doctor.Specialization = f
		doctor.Hospital = g
		doctor.Address = l
		doctor.Phone = h
		doctor.Email = i
		doctor.From = j
		doctor.To = k
		doctor.save()
		j=True
	return render(request,'add doctor.html',{'j': j})

def blog(request):
	return render(request,'index.html')

def view(request):
	doctor=Doctors.objects.all()
	return render(request,'available.html',{'doctor' : doctor})

def find(request):
	a=str(request.POST.get('find'))
	doctor=Doctors.objects.filter(Name=a)
	return render(request,'available.html',{'doctor' : doctor})

def delete(request):
	a=request.POST.get("subject")
	Doctors.objects.filter(Phone=a).delete()
	doctor=Doctors.objects.all()
	return render(request,'available.html',{'doctor' : doctor})

def dia(request):
	return render(request,'diabetes.html')
	"""a=request.POST.get("subject")
	Doctors.objects.filter(Phone=a).delete()
	doctor=Doctors.objects.all()
	return render(request,'available.html',{'doctor' : doctor})"""


def medical(request):
	j=False
	if(request.method=='POST'):
		a=request.POST.get('name')
		b=request.POST.get('age')
		c=request.POST.get('sex')
		d=request.POST.get('country')
		e=request.POST.get('email')
		f=request.POST.get('phone')
		g=request.POST.get('question')
		question=Questions()
		question.Name = a
		question.Age = b
		question.Sex = c
		question.Place = d
		question.Email = e
		question.Phone = f
		question.Problem= g
		question.save()
		j=True
	return render(request,'medicalhelp.html',{'j':j})

def tumor(request):
	return render(request,'breastcancer.html')

def hearts(request):
	return render(request,'heart.html')

def diavisual(request):
	make()
	global a,b,c,d,e,f,g,h,i
	i=0
	a=request.POST.get('pregnancies')
	b=request.POST.get('glucose')
	c=request.POST.get('bp')
	d=request.POST.get('skinthickness')
	e=request.POST.get('insulin')
	f=request.POST.get('bmi')
	g=request.POST.get('dpf')
	h=request.POST.get('age')
	return render(request,'visualization.html')

def diaresult(request):
	global a,b,c,d,e,f,g,h
	if(i==0):
		m="Possibility of not getting Diabetes is "
		n="Possibility of getting the Diabetes is "
		name="Diabetes Prediction in Women"
		accuracy,precision,recall,f1_score,output,positive,negative=check([[int(a),int(b),int(c),int(d),int(e),float(f),float(g),int(h)]])
	elif(i==1):
		m="Possibility of Benign Type Tumour is "
		n="Possibility of Malignant Type Tumour is "
		name="Breast Cancer Tumour Type"
		accuracy,precision,recall,f1_score,output,positive,negative=tumors([[float(a),float(b),float(c),float(d),float(e),float(f),float(g),float(h)]])
	else:
		m="Possibility of not getting Heart Disease is "
		n="Possibility of getting the Heart Disease is "
		name="Heart Disease Prediction"
		accuracy,precision,recall,f1_score,output,positive,negative=heart([[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h)]])

	return render(request,'output.html',{'x1':accuracy[0],'x2':accuracy[1],'x3':accuracy[2],'x4':accuracy[3],'x5':accuracy[4],'x6':accuracy[5],'x7':accuracy[6],'x8':accuracy[7],'x9':accuracy[8],
										'x10':precision[0],'x11':precision[1],'x12':precision[2],'x13':precision[3],'x14':precision[4],'x15':precision[5],'x16':precision[6],'x17':precision[7],'x18':precision[8],
										'x19':recall[0],'x20':recall[1],'x21':recall[2],'x22':recall[3],'x23':recall[4],'x24':recall[5],'x25':recall[6],'x26':recall[7],'x27':recall[8],
										'x28':f1_score[0],'x29':f1_score[1],'x30':f1_score[2],'x31':f1_score[3],'x32':f1_score[4],'x33':f1_score[5],'x34':f1_score[6],'x35':f1_score[7],'x36':f1_score[8],
										'x37':output[0],'x38':output[1],'x39':output[2],'x40':output[3],'x41':output[4],'x42':output[5],'x43':output[6],'x44':output[7],'x45':output[8],
										'x48':positive,'x47':negative,'name': name,'x49':m,'x50':n})

def tumorvisual(request):
	graph()
	global a,b,c,d,e,f,g,h,i
	i=1
	a=request.POST.get('pregnancies')
	b=request.POST.get('glucose')
	c=request.POST.get('bp')
	d=request.POST.get('skinthickness')
	e=request.POST.get('insulin')
	f=request.POST.get('bmi')
	g=request.POST.get('dpf')
	h=request.POST.get('age')
	return render(request,'visualization.html')

def heartvisuals(request):
	heartvisual()
	global a,b,c,d,e,f,g,h,i
	i=2
	a=request.POST.get('pregnancies')
	b=request.POST.get('glucose')
	c=request.POST.get('bp')
	d=request.POST.get('skinthickness')
	e=request.POST.get('insulin')
	f=request.POST.get('bmi')
	g=request.POST.get('dpf')
	h=request.POST.get('age')
	return render(request,'visualization.html')

		



