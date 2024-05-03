from django.db import models
from ckeditor.fields import RichTextField 
from django.contrib.auth.models import User


# Create your models here.
class Courses(models.Model):
    courseName=models.CharField(max_length=150,primary_key=True)
    image=models.ImageField(upload_to="course",blank=True,null=True)
    courseFee=models.IntegerField()
    courseDuration=models.IntegerField()
    syllabus=RichTextField(default="syllabus")
    aboutCourse=RichTextField(default="aboutCourse")
    stars=models.IntegerField(default=3)

    def __str__(self):                         #one linear function
        return self.courseName


class Trainer(models.Model):
    trainer_name=models.CharField(max_length=50)
    trainer_designation=models.CharField(max_length=100)
    trainer_experience=models.DecimalField(max_digits=5,decimal_places = 2)
    course=models.ForeignKey(Courses,on_delete=models.SET_NULL, null = True)
    def __str__(self):
        return self.trainer_name



class Register(models.Model):
    candidateId=models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    fatherName=models.CharField(max_length=20)
    phoneNumber=models.CharField(max_length=14)
    alternateNumber=models.CharField(max_length=14)
    email=models.EmailField(unique=True)
    collegeName=models.CharField(max_length=100)
    address=models.TextField(max_length=150)
    landmark=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.IntegerField()
    companyName=models.CharField(max_length=150,blank=True,null=True)
    designation=models.CharField(max_length=150)
    qualification=models.CharField(max_length=100)
    computerKnowledge=models.CharField(max_length=50)
    Course=models.CharField(max_length=150)
    timestamp = models.DateField(auto_now_add=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.DO_NOTHING,null=True)
    
    def __str__(self):
        return self.email


class Payments(models.Model):
    name=models.ForeignKey(Register,on_delete=models.CASCADE)
    amountPaid=models.IntegerField()
    balance=models.IntegerField(blank=True,null=True)
    status= models.CharField(max_length=20,default="Unpaid")
    def __int__(self):
        return self.name
    

class Attendace(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    date=models.CharField(max_length=50)
    logintime=models.CharField(max_length=50)
    logouttime=models.CharField(max_length=50)
    approved=models.BooleanField(default=False)
    def __str__(self):
        return self.email
    
    
    
    
    

# FREELANCING___________________


class Freelancer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    skills = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ClientOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


# class Client(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     # Add more fields as needed

