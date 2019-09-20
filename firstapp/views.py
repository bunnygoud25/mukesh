from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request,'index.html')
def hire(request):
    return render(request,'hire.html')
