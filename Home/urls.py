from django.urls import path
from .views import Home

app_name = 'homeapp'

urlpatterns =[
    path('',Home,name='index'),
    
]
