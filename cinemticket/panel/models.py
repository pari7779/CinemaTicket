from django.db import models
from movie.models import Movie, Sans

# Create your models here.
class Ticket(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, related_name='ticket_movie_detail')
    date_movie = models.ForeignKey(to=Sans, on_delete=models.CASCADE, related_name='ticket_movie_date')
    time_buy = models.DateTimeField()
    price = models.IntegerField()

class Transaction(models.Model):
    transaction = models.IntegerField()
    time_buy = models.DateTimeField()

class Wallet(models.Model):
    amount = models.IntegerField()
    history = models.ForeignKey(to=Transaction, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    birthday = models.DateField()
    wallet = models.IntegerField()
    my_ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True)




