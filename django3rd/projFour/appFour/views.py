from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request,'appFour/index.html')

# def greet(request, name):
#   return HttpResponse(f'Hello {name.capitalize()}')

def greet2(request, name):
  return render(request,'appFour/greet2.html',{
    'name':name.capitalize()
  })