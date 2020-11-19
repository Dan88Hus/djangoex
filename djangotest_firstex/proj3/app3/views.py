from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
  task = forms.CharField(label='New Task')
  # priority = forms.IntegerField(label='Priority', max=10)


# reason to delete tasks in here is to make session
# it will be under index function
# tasks = [ 'foo' ]

# to create table in django
# python manage.py migrate



def index(request):
  if 'tasks' not in request.session:
    request.session['tasks'] = []
  return render(request, 'app3/index.html', {
    'tasks' : request.session['tasks']
  })

def add(request):
  if request.method == 'POST':
    form = NewTaskForm(request.POST)
    if form.is_valid():
      task = form.cleaned_data['task']
      request.session['tasks'] += [task]
      return HttpResponseRedirect(reverse('app3:index'))
    else:
      return render(request,'app3/add.html',{
        'form':form
      })
  return render(request, 'app3/add.html', {
    "form":NewTaskForm()
  })
