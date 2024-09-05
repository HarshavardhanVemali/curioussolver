from django.shortcuts import render
from django.http import JsonResponse
from .models import Register

def index(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')

def registerpage(request):
    return render(request,'register.html')

def researchpaper(request):
    return render(request,'researchpaper.html')

def websitedevelopment(request):
    return render(request,'websitedevelopment.html')

def patents(request):
    return render(request,'patents.html')

def courses(request):
    return render(request,'courses.html')

def internships(request):
    return render(request,'internships.html')

def register(request):
    if request.method=='POST':
        student_name=request.POST.get('student_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        if not(student_name and email and phone_number):
            return JsonResponse({'success':False,'message':'Required missing fields.'})
        if Register.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'success':False,'message':'User already exists.'})
        register = Register(
            name=student_name,
            phone_number=phone_number,
            email=email
        )
        register.save()
        if register.pk:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Failed to register.'})
    else:
        return JsonResponse({'success':False,'message':'Invalid request method.'})