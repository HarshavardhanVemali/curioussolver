from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')