from os import listdir
from os.path import isfile, join

from django.http import HttpResponse
from django.shortcuts import redirect, render
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
    }
    template = loader.get_template('videos.html')
    return HttpResponse(template.render(context,request))



def music(request):
    music=media.objects.filter(category='music')
    context={
        'm':music,
    }
    template = loader.get_template('music.html')
    return HttpResponse(template.render(context,request))


def books(request):
    books=media.objects.filter(category='books')
    context={
        'b':books,
    }
    template = loader.get_template('books.html')
    return HttpResponse(template.render(context,request))


def updateDB():
    Video_present=media.objects.filter(category='videos')
    Music_present=media.objects.filter(category='music')
    Books_present=media.objects.filter(category='books')
    video_dir="etravel_search/static/images/media/videos"
    songs_dir="etravel_search/static/images/media/songs"
    books_dir="etravel_search/static/images/media/books"
    v=[f for f in listdir(video_dir) if isfile(join(video_dir, f))]
    s=[f for f in listdir(songs_dir) if isfile(join(songs_dir, f))]
    b=[f for f in listdir(books_dir) if isfile(join(books_dir, f))]

    V=[]
    M=[]
    B=[]
    for i in Video_present:
        S=i.media
        S=list(S.split('/'))
        V.append(S[-1])

    for i in Music_present:
        S=i.media
        S=list(S.split('/'))
        M.append(S[-1])
    
    for i in Books_present:
        S=i.media
        S=list(S.split('/'))
        B.append(S[-1])

    for i in v:
        if i not in V:
            a=media()
            a.name=list(i.split("."))[0]
            a.media="../../static/images/media/videos/"+i
            a.category="videos"
            a.save()
    
    for i in s:
        if i not in M:
            a=media()
            a.name=list(i.split("."))[0]
            a.media="../../static/images/media/songs/"+i
            a.category="music"
            a.save()

    for i in b:
        if i not in B:
            a=media()
            a.name=list(i.split("."))[0]
            a.media="../../static/images/media/books/"+i
            a.category="books"
            a.save()

updateDB()
