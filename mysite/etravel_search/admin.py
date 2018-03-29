from django.contrib import admin
from .models import Bus,User_Journey,Passenger

# Register your models here.

admin.site.register(Bus,name='Bus')
admin.site.register(User_Journey,name='User_Journey')
admin.site.register(Passenger,name='Passenger')

