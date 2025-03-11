from django.db import models

class Actor(models.Model): #related to Actors page#every related page shows description and 
    name = models.CharField(max_length=100)
    biography=models.TextField(max_length=1000)
    

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address=models.CharField(max_length=200)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    star = models.FloatField()
    vote = models.IntegerField()
    director_name = models.CharField(max_length=100)
    cast = models.ManyToManyField(Actor,related_name='movies')
    cinema = models.ForeignKey(to=Cinema,on_delete=models.CASCADE)
    

class Sans(models.Model):
    hall_number=models.models.models.CharField(max_length=50) #name or number
    date=models.DateTimeField()
    



    


    

