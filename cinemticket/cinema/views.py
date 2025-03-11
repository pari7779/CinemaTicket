from django.shortcuts import render
from django.http.response  import HttpResponse

# Create your views here.

def cinema_show(request):
    return HttpResponse("this is cinema page!!!")

def detail_movie(request):
    pass
