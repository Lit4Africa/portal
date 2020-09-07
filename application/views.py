# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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


@login_required
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


@login_required
def profile(request):
    """
    Load profile of logged in user
    :param request: HTTP request from client
    :return: render to correct template
    """
    user = request.user
    return render(request, 'profile.html', {'user_profile': user})


@login_required
def user_detail(request, pk):
    """
    Load profile of logged in user
    :param pk: Primary Key that identifies user's profile to be loaded
    :param request: HTTP request from client
    :return: render to correct template
    """
    if request.user.is_superuser:
        user_profile = User.objects.get(id=pk)
        return render(request, 'profile.html', {'user_profile': user_profile})
    else:
        return redirect('application:profile')


@login_required
def approve(request, pk):
    """
    Approve user application
    :param pk: Primary Key that identifies user to be approved
    :param request: HTTP request from client
    :return: render to correct template
    """
    if request.user.is_superuser:
        user = User.objects.get(id=pk)
        user.member.is_approved = True
        user.member.save()
        return redirect('application:user', pk)
    else:
        return redirect('application:profile')


@login_required
def disapprove(request, pk):
    """
    Disapprove user application
    :param pk: Primary Key that identifies user to be approved
    :param request: HTTP request from client
    :return: render to correct template
    """
    if request.user.is_superuser:
        user = User.objects.get(id=pk)
        user.member.is_approved = False
        user.member.save()
        return redirect('application:user', pk)
    else:
        return redirect('application:profile')


@login_required
def user_list(request):
    """
    Fetch all registered users to display
    :param request: HTTP request from client
    :return: render to correct template
    """
    approved = Member.objects.filter(is_approved=True)
    disapproved = Member.objects.filter(is_approved=False)
    pending = Member.objects.filter(is_approved=None,
                                    is_experienced_writer__in=['Y', 'N', 'M'])
    incomplete = Member.objects.filter(is_experienced_writer=None)
    return render(request, 'users.html', {'approved': approved,
                                          'disapproved': disapproved,
                                          'pending': pending,
                                          'incomplete': incomplete})
