from django.http.response import HttpResponse

# Create your views here.

def panel(response):
    return HttpResponse("پنل کاربری")

def my_ticket(response):
    return HttpResponse("بلیط های من")

def user(response):
    return HttpResponse("مشخصات من")

def buy_ticket(response):
    return HttpResponse("خرید بلیط")

def transactions(response):
    return HttpResponse("تراکنش های من")

def wallet(response):
    return HttpResponse("کیف پول")