from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
	context = {}
	return render(request, 'post/index.html', context)

@login_required(login_url='login')
def createPost(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')

	context = {}
	# return render(request, 'account/login.html', context)