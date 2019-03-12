from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>('google.com', 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0), ('seznam.cz', 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0), ('google.cz', 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0), ('gjk.cz', 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0)")
