from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=50)
    age = models. IntegerField()
    gender = models.CharField(max_length=30)
    height = models. IntegerField()
    weight = models. IntegerField()
    symptom1 = models.CharField(max_length=30)
    symptom2 = models.CharField(max_length=30, blank=True)
    symptom3 = models.CharField(max_length=30, blank=True)
    symptom4 = models.CharField(max_length=30, blank=True)
    symptom5 = models.CharField(max_length=30, blank=True)
    disease = models.CharField(max_length=30)
    consultDoctor = models.CharField(max_length=30)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)


    def __str__(self):
        return self.name


class newuser(models.Model):
    
    my_id = models.CharField(primary_key=True, max_length=10,default='')
    Username=models.CharField(max_length=80)
    fname=models.CharField(max_length=89)
    lname=models.CharField(max_length=88)
    email=models.EmailField(max_length=90)
    pass1=models.CharField(max_length=90)
    pass2=models.CharField(max_length=90)

class Doctorinfo(models.Model):
    SEMESTER_CHOICES = (
        ("1", "Neurologist"),
        ("2", "Allergist_Immunologist"),
        ("3", " Urologist"),
        ("4", "Dermatologist"),
        ("5", " Gastroenterologist"),
     
        )
    fname=models.CharField(max_length=89)
    lname=models.CharField(max_length=88)
    Username=models.CharField(max_length=80)
    pass1=models.CharField(max_length=90)
    email=models.EmailField(max_length=90)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=120)
    specialization=models.CharField(max_length=180)
    
    
class reportd(models.Model):
    name=models.CharField(max_length=190)
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    height=models.CharField(max_length=10)
    weight=models.CharField(max_length=10)
    symptom1=models.CharField(max_length=120)
    symptom2=models.CharField(max_length=120)
    symptom3=models.CharField(max_length=120)
    symptom4=models.CharField(max_length=120)
    symptom5=models.CharField(max_length=120)
    predicted_disease=models.CharField(max_length=120)
    consultdoctor=models.CharField(max_length=120)


class student(models.Model):
    
    aadhaarno = models.CharField( max_length=10,default='')
    # Username=models.CharField(max_length=80)
    fname=models.CharField(max_length=89)
    lname=models.CharField(max_length=88)
    email=models.EmailField(max_length=90)
    pass1=models.CharField(max_length=90)
    pass2=models.CharField(max_length=90)


class patientdec(models.Model):
    aadhaarno=models.CharField(max_length=25,default='')
    name=models.CharField(max_length=190)
    lname=models.CharField(max_length=190)
    symptoms1=models.CharField(max_length=200)
    symptoms2=models.CharField(max_length=200)
    symptoms3=models.CharField(max_length=200)
    symptoms4=models.CharField(max_length=200)
    Disease=models.CharField(max_length=200)
    Medicine=models.CharField(max_length=200)
    date=models.DateField(max_length=200)
    hphone=models.CharField(max_length=10)
    file=models.FileField(upload_to="document/",default='0')
    

    


