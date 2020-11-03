from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

@login_required(login_url='login')
def index(request):
	context = {
        'posts': Post.objects.all().order_by('-date_created')
    }
	return render(request, 'post/main.html', context)

@login_required(login_url='login')
def createPost(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')

	context = {}
	return render(request, 'account/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'post/main.html'
    context_object_name = 'posts'
    ordering = ['-date_created']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post/create.html'

