from django.urls import path
from .views import panel, my_ticket, user, buy_ticket, transactions, wallet

urlpatterns = [
    path('', panel),
    path('my-tickets', my_ticket),
    path('profile', user),
    path('buy-ticket', buy_ticket),
    path('transactions', transactions),
    path('wallet', wallet)
]