from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request, 'index.html')

def contactus(request):
    return render(request, 'contactus.html')


def course(request):
    return render(request, 'course.html')

def explore(request):
    return render(request, 'explore.html')