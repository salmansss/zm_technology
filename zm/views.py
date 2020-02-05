from django.shortcuts import render
from django.http import HttpResponse
from .models import batches

# Create your views here.

def index(request):

    return render(request, 'index.html')

def contactus(request):
    return render(request, 'contactus.html')


def course(request):
    return render(request, 'course.html')

def explore(request):
    return render(request, 'explore.html')

def zm_branch(request):

    batches1 = batches.objects.all()
    return render(request, 'zm_branch.html',{'batches1': batches1})