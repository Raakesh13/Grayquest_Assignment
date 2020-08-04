from django.shortcuts import render, redirect, reverse
from meme_viewer.signinform import LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Cookies
from django.contrib.auth.models import User
from django.http import HttpResponse
import requests
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    if len(request.session.items()) == 0:
        return redirect('login')

    try:
        cookie_status = Cookies.objects.get(
            user_id=User.objects.get(username=request.session['username']).id)
        request.session.set_expiry(1800)
    except:
        cookie_status = Cookies.objects.create(
            user_id=User.objects.get(username=request.session['username']).id)
        request.session.set_expiry(1800)

    try:
        req = requests.get("https://api.imgflip.com/get_memes")
        memeListJSON = req.json()
        memeList = memeListJSON['data']['memes'][:5]

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        return HttpResponse('Check internet connection', status=500)

    return render(request, 'home.html', {'sessioninfo': {'username': request.session['username'], 'session_expiry_age': request.session.get_expiry_age()}, 'cookie_status': cookie_status.setCookies, 'memeList': memeList})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # context['username'] = 'Rakesh'
            request.session['username'] = str(user)
            # print(type(user))
            # print(request.session.keys())
            # print(request.session.get_session_cookie_age())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    # print(request.method)
    # if request.method == 'POST':
    logout(request)
    return redirect('login')
    # return HttpResponse('<h1>Logged out</h1>')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # context['username'] = 'Rakesh'
            request.session['username'] = str(user)
            # print(type(user))
            # print(request.session.keys())
            # print(request.session.get_session_cookie_age())
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def update_cookie_status(request):
    cookie_status = Cookies.objects.get(
        user_id=User.objects.get(username=request.session['username']).id)
    cookie_status.setCookies = True
    cookie_status.save()
    return HttpResponse('1')
