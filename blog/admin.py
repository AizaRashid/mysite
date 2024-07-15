from django.contrib import admin
from .models import Post, Comment,Category,Profile
from django.contrib.auth.models import User
from django.contrib.admin.options import ModelAdmin
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
	model=Profile

