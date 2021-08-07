from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model):

    GENDER_CHOICES = [('Male', 'Male'),('Female', 'Female')]  #[(tuple)], ('Male', 'Male') one for desply one male for value
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True, blank = True)
    dob = models.DateField(default = datetime.now, blank = True)
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, default = 'Male', )
    def __str__(self):
        return f"Id: {self.id} Name: {self.name}"
