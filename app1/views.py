from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%d-%m-%Y %H:%M:%S %p", gmtime())
    }
    return render(request,'index.html', context)