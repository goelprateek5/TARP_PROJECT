from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Cost
from etravel_search.models import User_Journey,Passenger
import serial
import time

# Create your views here.


def Ard(I):
    ser=serial.Serial("/dev/ttyACM0",9600)
    serin =ser.readline()
    serin=str(serin)[2:9]
    #ser.close()

    if str(I)==str(serin):
        return True,serin
    else:
        return False,serin


def index(request):
    template=loader.get_template('index1.html')
    J_ID=1 #different for every bus
    l=User_Journey.objects.all().filter(Journey_id=1)
    C=Cost.objects.all().filter(J_ID=1)
    Pass=Passenger.objects.all()
    price=0
    User_name='Welcome Mr. '
    for i in C:
        if(i.J_ID==str(J_ID)):
            price=i.Price
            break

    S="Access Denied"
    for i in range(len(l)):
        record=l[i]
        I=record.id
        U=record.User_id
        J=record.Journey_id
        if int(J)==J_ID:
            flag,serin=Ard(U)
            User=Pass.filter(User_id=serin)
            for k in User:
                User_name += k.User_name
            if (flag) and len(User)!=0 and record.Session_id==False :
                for h in Pass:
                    if(h.User_id==serin):
                        # User_name = h.User_name
                        h.Credit=str(int(h.Credit)-int(price))
                        if(int(h.Credit)<0):
                            flag=False
                            S="Insufficient balance. Kindly Recharge to proceed."
                        else:
                            h.save(update_fields=["Credit"])
                if(flag):
                    S="Access Granted"
                    record.Session_id=True
                    record.save(update_fields=["Session_id"])
                    break
            elif len(User)==0:
                S = "Not a registered User."
                User_name = ''
    context={
        'S':S,
        'U':User_name,
    }

    # time.sleep(5)
    return HttpResponse(template.render(context,request))

    # except:
    #     return HttpResponse("<h1>No RFID Reader Connected</h1>")



