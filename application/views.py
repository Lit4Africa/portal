# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from application.models import Member


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        fav_color = request.POST['fav_color']
        DOB = request.POST['DOB']
        password = request.POST['password']
        address = request.POST['address']
        about = request.POST['about']
        image = request.FILES['image']
        gender = request.POST['gender']

        user = User.objects.create_user(username=username, email=email,
                                        password=password,
                                        first_name=first_name,
                                        last_name=last_name)
        user.save()
        member = Member.objects.create(user=user, fav_color=fav_color,
                                       DOB=DOB, address=address, about=about,
                                       image=image, gender=gender)
        member.save()
        return redirect('application:login')
    elif request.method == 'GET':
        return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('application:profile')
        else:
            # Return an 'invalid login' error message.
            ...
    elif request.method == 'GET':
        return render(request, 'login.html')


def apply(request):
    if request.method == 'POST':
        return redirect('application:login')
    elif request.method == 'GET':
        return render(request, 'application-form.html')


def logout_view(request):
    logout(request)
    return redirect('application:login')
