from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
# models.py  

    
class Category(models.Model):
    name =  models.CharField(max_length=255,unique=True)

    def get_absolute_url(self):
        return reverse("post_list")
    def __str__(self):
        return self.name
 
class Profile(models.Model):
    email = models.EmailField(max_length=50,default="username@gmail.com")
    first_name = models.CharField(max_length=50,default="FirstName")
    last_name = models.CharField(max_length=50,default="Lastname")
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="user")
    bio = models.CharField(blank=True,null=True,max_length=50)
    description=RichTextField(blank=True,null=True)
    followers = models.ManyToManyField('self',related_name='following',symmetrical=False,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile/")
    website_url= models.CharField(max_length=200,null=True,blank=True)
    facebook_url = models.CharField(max_length=200,null=True,blank=True)
    twitter_url = models.CharField(max_length=200,null=True,blank=True)
    insta_url = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.user)
        
    @receiver(post_save,sender=User)
    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

            

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=255,default='title tag')
    header_image = models.ImageField(null=True,blank=True,upload_to="header_images/")
    alt_text = models.CharField(max_length=255,blank=True,null=True)
    text = RichTextField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=200,default='coding')
    snippet = models.CharField(max_length=100,default="Click on the link below to read full article...",null=True,blank=True)
    likes = models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title + '|' + str(self.author)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(User,max_length=200)
    text = RichTextField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
