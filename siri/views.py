from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sai(request):
    return HttpResponse('<h1>hellooo</h1>')