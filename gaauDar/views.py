from django.shortcuts import render
from .forms import IcalcForm

def interestCalculate(request):
    form = IcalcForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        form = IcalcForm()
    
    return render(request,'index.html',{'form':form })

def keepRecord(request):

    return render(request,'recordMenu.html')

def transaction(request):
    return render(request,'transit.html')

def interestRate(request):
    
    return render(request,'rateInfo.html')

