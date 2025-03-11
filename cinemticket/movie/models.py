from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    star = models.FloatField()
    vote = models.IntegerField()
    director_name = models.CharField(max_length=100)
    cast = models.ManyToManyField(Actor,related_name='movies')
    cinema = models.ForeignKey(to=Cinema)
    
    
class Sans(models.Model):
    pass

class Ticket(models.Model):
    pass

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    

class Actor(models.Model): #related to Actors page#every related page shows description and 
    name = models.CharField(max_length=100)
    biography=models.TextField(max_length=1000)
    movie=models.ManyToManyField(Movie)    

