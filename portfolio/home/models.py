from statistics import mode
from django.db import models
from flask_sqlalchemy import Model

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    ctc = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
    
class Viewer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, primary_key = True)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.email