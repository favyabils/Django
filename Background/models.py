from django.db import models


# Create your models here.

class Person(models.Model): #"Person" is a table
#"name" is a column
    name =  models.CharField(max_length=150) #"models."fieldname"()Tells the type of datatype that can be stored in the column "name
    age = models.IntegerField()
    occupation = models.CharField(max_length= 200)
