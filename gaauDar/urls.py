from django.urls import path
from .views import interestCalculate,keepRecord,transaction,interestRate

app_name= 'app1'

urlpatterns =[
    path('interestCalculate/',interestCalculate,name='interestCalculate'),
    path('keepRecord/',keepRecord,name='keepRecord'),
    path('transaction/',transaction,name='transaction'),
    path('interestRate',interestRate,name='interestRate'),
    
    
]
