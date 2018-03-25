from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import media


# Create your views here.

def index(request):

    # all_buses=Bus.objects.all()
    # template=loader.get_template('home_page/index.html')
    # context={
    #     'all_buses':all_buses,
    # }
    return render(request, 'mediaAccess.html')
    # return HttpResponse(template.render(context,request))

def videos(request):
    video = media.objects.filter(category='videos')
    context = {
    'v':video,
    'vpath': '/media/'
    }
    template = loader.get_template('videos.html')
    return HttpResponse(template.render(context,request))



def music(request):
    return render(request, 'music.html')


def books(request):
    return render(request, 'books.html')

