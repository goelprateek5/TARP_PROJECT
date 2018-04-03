from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Bus,Passenger,User_Journey
from rfid.models import Cost
from datetime import datetime
import time


# def callme():
#     time.sleep(5)
#     return redirect('127.0.0.1:8000/')


def index(request):
    all_buses=Bus.objects.all()
    template=loader.get_template('home_page/index.html')
    G=Bus.objects.all().filter(J_ID='ads')
    if request.method=='POST':
        S_t=request.POST['To']
        S_f=request.POST['From']
        S_d=request.POST['date']
        dt_obj=datetime.strptime(S_d,'%Y-%m-%d').date()
        S_d=dt_obj.strftime('%d-%m-%Y')

        
    # return redirect('https://bus.makemytrip.com/bus/search/'+S_f+'/'+S_t+'/'+S_d)

        C=Cost.objects.filter(From_city=S_f).filter(To_city=S_t)
        for c in C:
            G=Bus.objects.filter(J_ID=c.J_ID)
                    
    
    
    context={
        'all_buses':all_buses,
        'G':G,
    }
    #return render(request, 'home_page/home.html')
    return HttpResponse(template.render(context,request))






def confirm(request):
    S=request.POST.get('busid',"")
    R=request.POST.get('rfid',"")
    alert=True
    context={
        'S':S,
        'R':R,
        'alert':alert,
        # 'callme':callme(),
    }

    User=User_Journey()
    User.Journey_id=S
    User.User_id=R
    User.Session_id=False
    User.save()
    return render(request,'home_page/book.html',context)