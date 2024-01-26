from django.db import models

# Create your models here.
#models are classes, one model for each of teh tables we care about 

class Flight(models.Model):
    #inheriting from the class Model on django 

    #defining all the properties that a flight has 
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.origin} to {self.destination} {self.duration}"