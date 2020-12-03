from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def expressentryform(request):
    return render(request, 'expressentryform.html')

def thankyou(request):
        return render(request, 'thankyou.html')
