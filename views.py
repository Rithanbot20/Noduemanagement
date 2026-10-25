from django.shortcuts import render
from . models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html',{})
def alerts(request):
    return render(request,'alerts.html',{})
def blank(request):
    return render(request,'blank.html',{})
def create_agent(request):
    return render(request,'create_agent.html',{})
def footer(request):
    return render(request,'footer.html',{})
def forgot_password(request):
    return render(request,'forgot_password.html',{})
def forms(request):
    return render(request,'forms.html',{})
def header(request):
    return render(request,'header.html',{})
def login(request):
    return render(request,'login.html',{})
def profile(request):
    return render(request,'profile.html',{})
def register(request):
    return render(request,'register.html',{})
def settings(request):
    return render(request,'settings.html',{})
def subject(request):
    return render(request,'subject.html',{})
def homepage(request):
    return render(request,'home_page.html',{})
def registerpage(request):
    if request.method == 'POST':
        a = request.POST.get('fname')
        b = request.POST.get('rno')
        c = request.POST.get('mail')
        d=request.POST.get('dept')
        e=request.POST.get('year')
        f=request.POST.get('addr')
        g=request.POST.get('psw')
        crt = Student.objects.create(first_name=a, roll_no=b,
        email=c,department=d,year=e,address=d,password=g)
        if crt:
            messages.success(request,'Register Successfully')

    return render(request,'register_page.html',{})
def loginpage(request):
    return render(request,'login_page.html',{})
def aboutpage(request):
    return render(request,'about_page.html',{})
def contactpage(request):
    return render(request,'contact_page.html',{})
def footerpage(request):
    return render(request,'footer_page.html',{})


