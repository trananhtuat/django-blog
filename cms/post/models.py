from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200, null=True)
	content = models.TextField(null=True)
	# post_image = models.ImageField()
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	def __str__(seft):
		return seft.title
	def get_absolute_url(self):
		 return reverse('post-detail', kwargs={'pk': self.pk})