from django.shortcuts import render
import datetime

# Create your views here.
def newyear(request):
  now = datetime.datetime.now()
  return render(request, 'appFour/date.html', {
    'newyear': now.month == 1 and now.day == 1 
  })
