from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('post')
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			return redirect('login')
	context = {'form': form}
	return render(request, 'account/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('post')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('post')
		else:
			messages.info(request, 'Username or password is incorrect!')
	context = {}
	return render(request, 'account/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

# @login_required(login_url='login')
# def home(request):
# 	context = {}
# 	return render(request, 'account/home.html', context)