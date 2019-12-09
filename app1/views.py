from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')

def aa(request):
    return render(request,'aa.html')

def index(request):
    return render(request,'index.html')