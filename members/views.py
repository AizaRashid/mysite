from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView,CreateView,DetailView,DetailView
from .forms import EditProfileForm,SignUpForm
from blog.models import Profile,Comment,Post,Category
from .forms import PasswordChangingForm,ProfilePageForm,EditProfileForm,SignUpForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.contrib.auth.decorators import login_required
# Cr eate your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('post_list')
        else:
            # Return an 'invalid login' error message.
            messages.success(request,("There was an error logging in, Try again!"))
            return redirect('post_list')
    else:
        return render(request,'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("You were Logged Out!"))
    return redirect('post_list')


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('Registration Successful!'))
            return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request,"authenticate/register_user.html",{'form':form,})


class CreateProfilePageView(CreateView):
    fields ='__all__'
    model= Profile
    template_name = 'authenticate/create_user_profile.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

    # success_url = reverse_lazy('home')

def password_success(request):
    success_url = reverse_lazy('post_list')
    return render(request, 'authenticate/password_success.html', {})


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'authenticate/edit_profile_page.html'
    success_url = reverse_lazy('post_list')
    fields='__all__'
    def get_object(self):
        return self.request.user.profile

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        posts = Post.objects.filter(author=profile.user)
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST["follow"]
            if action == "unfollow":
                current_user_profile.followers.remove(profile)
            else:
                action =='follow'
                current_user_profile.followers.add(profile)
            current_user_profile.save()

        return render(request,'authenticate/profile.html',{"profile":profile,"posts":posts})
    else:
        messages.success(request,("You must be Logged In to see this page!"))
        return redirect('post_list')
