from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def holamundo(requuest):
   return HttpResponse('Hola Mundo')
