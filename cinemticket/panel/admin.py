from django.contrib import admin
from panel.models import *
# Register your models here.
admin.site.register(Ticket)
admin.site.register(Transaction)
admin.site.register(Wallet)
admin.site.register(User)