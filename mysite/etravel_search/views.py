from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Bus,Search
from rfid.models import Cost
from .forms import SearchForm
from datetime import datetime

# Create your views here.
def index(request):
    all_buses=Bus.objects.all()
    template=loader.get_template('home_page/index.html')
    context={
        'all_buses':all_buses,
    }
    #return render(request, 'home_page/home.html')
    return HttpResponse(template.render(context,request))



def save_req(request):
    if request.method=='POST':
        S=SearchForm(request.POST)
        S_t=request.POST['To']
        S_f=request.POST['From']
        S_d=request.POST['date']
        dt_obj=datetime.strptime(S_d,'%Y-%m-%d').date()
        S_d=dt_obj.strftime('%d-%m-%Y')

        if(S.is_valid()):
            S.save()
    # return redirect('https://bus.makemytrip.com/bus/search/'+S_f+'/'+S_t+'/'+S_d)

    C=Cost.objects.filter(From_city=S_f).filter(To_city=S_t)
    for c in C:
        G=Bus.objects.filter(J_ID=c.J_ID)
                    
    
    context={
        'G':G,
    }

    return render(request,'home_page/booking.html',context)




