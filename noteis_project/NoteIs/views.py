from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from pyexpat.errors import messages

from .database import Database, auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

data =Database()

def home(request):
    return render(request,"noteisapp/home.html")

def login_page_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)

            if user:
                request.session['uid'] = user['localId']
                return render(request, 'noteisapp/home.html')
            else:
                error_message = "Geçersiz email veya şifre. Lütfen tekrar deneyin."
                return render(request, 'noteisapp/login.html', {'error_message': error_message})

        except Exception as e:
            error_message = "Bir hata oluştu: {}".format(str(e))
            return render(request, 'noteisapp/login.html', {'error_message': error_message})
    else:
        return render(request, 'noteisapp/login.html')

def register_page_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            data.register(email, password)
            return render(request, 'noteisapp/home.html')
        except Exception as e:
            error_message = "Bir hata oluştu: {}".format(str(e))
            return render(request, 'noteisapp/register.html', {'error_message': error_message})
    else:
        return render(request, 'noteisapp/register.html')
    


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = auth.sign_in_with_email_and_password(email, password)

            if user:
                request.session['uid'] = user['localId']
                return render(request, 'noteisapp/home.html')
            else:
                error_message = "Geçersiz email veya şifre. Lütfen tekrar deneyin."
                return render(request, 'login.html', {'error_message': error_message})

        except Exception as e:
            error_message = "Bir hata oluştu: {}".format(str(e))
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')



def register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            data.register(email, password)
            return render(request, 'noteisapp/home.html')
        except Exception as e:
            error_message = "Bir hata oluştu: {}".format(str(e))
            return render(request, 'register.html', {'error_message': error_message})
    else:
        return render(request, 'register.html')
