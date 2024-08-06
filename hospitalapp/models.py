from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
#when done with the def and everything ensure you go to models admin to register it
    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    date = models.DateField()
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
class Member(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname