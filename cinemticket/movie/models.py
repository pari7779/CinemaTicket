from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    star=models.FloatField()
    rate=models.IntegerField()
    


class Sans(models.Model):
    pass

class Ticket(models.Model):
    pass

