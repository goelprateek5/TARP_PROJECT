from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from rfid.models import Cost

def index(request):
	c=Cost.objects.all().filter(J_ID='1')
	t=''
	for i in c:
		f=i.From_city
		t=i.To_city
	template = loader.get_template('loc.html')
	context={
	't':t,
	'f':f,
	}
	return HttpResponse(template.render(context,request))
	# return render(request,'loc.html')