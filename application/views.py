# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from application.models import *


def register(request):
    """
    Navigate to register.html or handle POST request and create new user.
    :param request: HTTP request from client
    :return: render to correct template
    """
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
    """
    Navigate to login.html or handle POST request and log in user.
    :param request: HTTP request from client
    :return: render to correct template
    """
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
    """
    Navigate to application-form.html or handle POST request and submit user
    application
    :param request: HTTP request from client
    :return: render to correct template
    """
    if request.method == 'POST':
        user = request.user
        member = Member.objects.get(user=user)
        member.objectives.set(request.POST['objectives'])
        member.teams.set(request.POST['teams'])
        member.idea_promote_reading = request.POST['idea_promote_reading']
        member.idea_project_successful = request.POST[
            'idea_successful_project']
        member.idea_achieve_objectives = request.POST[
            'idea_achieve_objectives']
        member.is_experienced_writer = request.POST['is_writer']
        member.idea_funding = request.POST['idea_funding']
        member.can_donate_for_bookdrive = request.POST['can_donate']
        member.thoughts_on_writing_space = request.POST['create_space']
        member.save()
        return redirect('application:login')
    elif request.method == 'GET':
        teams = Team.objects.all()
        objectives = Objective.objects.all()
        return render(request, 'application-form.html',
                      {'teams': teams, 'objectives': objectives})


def logout_view(request):
    """
    Log user out
    :param request: HTTP request from client
    :return: render to correct template
    """
    logout(request)
    return redirect('application:login')


def profile(request):
    """
    Load profile of logged in user
    :param request: HTTP request from client
    :return: render to correct template
    """
    user = request.user
    return render(request, 'profile.html', {'user': user})
