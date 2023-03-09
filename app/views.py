from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def suresh(request):
    return HttpResponse('<h1>hiiiiiii</h1>')
