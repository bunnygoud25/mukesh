from django.shortcuts import render,redirect
from .forms import contactForm


def message(request):
    form= contactForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'sent.html')
# Create your views here.
