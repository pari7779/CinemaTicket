from django.urls import path
from .views import cinema_show,detail_movie

urlpatterns = [
    
    path('cinema',cinema_show),
    path('detail/<str:id>',detail_movie)
    
    
]


