from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from playground.models import WebPage, Topic

def index(request):
    # my_dict = { 'insert_me' : "HEllO IM x DYNAMIC"}
    x = Topic.objects.all
    my_dict = { 'topics' : x }
    return render(request,'playground/index.html',context  = my_dict)


def help(request):
    d1 = { 'd' : 'context must be a dict!'}
    return render(request, 'playground/help.html' , context= d1)