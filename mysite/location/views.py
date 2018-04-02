from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from rfid.models import Cost

def index(request):
	c=Cost.objects.all().filter(J_ID='1')
	t=''
	for i in c:
		t=i.To_city
	template = loader.get_template('loc.html')
	context={
	'c':t,
	}
	return HttpResponse(template.render(context,request))
	# return render(request,'loc.html')