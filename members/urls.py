from django.urls import path
from members.views import (login_user,logout_user,sign_up,EditProfilePageView,password_success,
CreateProfilePageView,PasswordsChangeView,profile)
urlpatterns = [
   path('login_user',login_user,name='login_user'),
   path('logout_user',logout_user,name='logout_user'),
   path("sign_up/",sign_up,name='sign_up'),
   path("<int:pk>/edit_profile_page/",EditProfilePageView.as_view(),name="edit_profile_page"),
   path("password_success/",password_success,name='password_success'),
   path("create_profile_page/<int:pk>",CreateProfilePageView.as_view(),name="create_profile_page"),
   path("password_change/",PasswordsChangeView.as_view(template_name='authenticate/change_password.html'),name='change_password'),
   path('<int:pk>/profile/',profile,name='profile'),
]