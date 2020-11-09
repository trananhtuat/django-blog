from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

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

# @login_required(login_url='login')
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url='login'

    model = Post
    fields = ['title', 'content']
    template_name = 'post/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

