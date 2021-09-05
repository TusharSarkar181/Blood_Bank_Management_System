from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    reg_first_name = models.CharField(max_length=150)
    reg_last_name = models.CharField(max_length=150,default='SOME STRING')
    reg_email = models.CharField(max_length=200)
    reg_password = models.CharField(max_length=20)
    reg_confirm_pass = models.CharField(max_length=20)
    
def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=30,blank=False)
    email = models.EmailField(max_length=30,blank=False)
    phone_number = models.IntegerField(blank=False)
    messege = models.CharField(max_length=300,blank=False)
   
def __str__(self):
        return self.phone_number

class DonorRegister(models.Model):
    dreg_first_name = models.CharField(max_length=150)
    dreg_last_name = models.CharField(max_length=150,default='SOME STRING')
    dreg_email = models.CharField(max_length=200)
    dreg_password = models.CharField(max_length=20)
    dreg_password = models.CharField(max_length=20)
    dreg_date_of_birth = models.CharField(max_length=20)
    dreg_phone_number = models.IntegerField()

def __str__(self):
        return self.name

class PaymentGateway(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    payment_method = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)

def __str__(self):
    return self.subject



class Donation(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)

    BLOOD_CHOICE =(
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),

    )
    bloodgroup = models.CharField(max_length=100, choices=BLOOD_CHOICE)

    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)

def __str__(self):
    return self.name
