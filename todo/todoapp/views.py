from django.shortcuts import render
from todoapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, get_user_model
from todoapp.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todoapp.models import Todolist
import json


def Coaches(request):
    return render(request, 'Coaches.html')


def index(request):
    return render(request, 'index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Coaches'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                if user.is_active:
                    return HttpResponse("Your account was inactive.")
        except:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(email, password))
            return HttpResponse("Invalid login details given")

    return render(request, 'login.html', {})


@api_view(['GET', 'POST'])
def addtodo(request):
    if request.method == 'POST':
        login_details = json.loads(request.body)
        print(login_details)
        id = login_details.get('id', None)
        taskname = login_details.get('taskname', None)
        status1 = login_details.get('status', None)
        todo = Todolist()
        todo.taskname = taskname
        todo.status = status1
        print('****')
        print(todo.status)
        print(todo.taskname)
        print('****')
        todo.save()
    return Response({'key': 'value'}, status=status.HTTP_200_OK)