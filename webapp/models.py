from django.db import models

# Create your models here.
class Doctors(models.Model):

	
	Name = models.CharField(max_length=30)
	Age = models.CharField(max_length=2)
	Qualification = models.CharField(max_length=30)
	Experience = models.CharField(max_length=2)
	Gender = models.CharField(max_length=15)
	Specialization = models.CharField(max_length=30)
	Hospital = models.CharField(max_length=50)
	Address = models.CharField(max_length=100)
	Phone = models.CharField(max_length=15)
	Email = models.CharField(max_length=30)
	From = models.TimeField()
	To = models.TimeField()
	
	def __str__(self):
		return str(self.Name + self.Specialization)

class Questions(models.Model):

	Name = models.CharField(max_length=30)
	Age = models.CharField(max_length=2)
	Sex = models.CharField(max_length=15)
	Place = models.CharField(max_length=50)
	Email = models.CharField(max_length=30)
	Phone = models.CharField(max_length=15)
	Problem= models.CharField(max_length=2000)

	def __str__(self):
		return str(self.Problem)

class Answers(models.Model):

	Name = models.CharField(max_length=30)
	Hospital = models.CharField(max_length=50)
	Phone = models.CharField(max_length=15)
	patientname= models.CharField(max_length=30)
	patientnumber= models.CharField(max_length=15)
	Problem= models.CharField(max_length=2000)
	Answer= models.CharField(max_length=2000)
	Medicine= models.CharField(max_length=2000)

	def __str__(self):
		return str(self.Hospital)
