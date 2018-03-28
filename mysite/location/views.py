from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

def index(request):
	return render(request,'loc.html')