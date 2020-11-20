from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # to take 'name' parameter as argument 
    # we need to use converter ie<str:name> in this case
    # path('<str:name>', views.greet, name='greet'),
    path('<str:name>', views.greet2, name='greet2'),


]