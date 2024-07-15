from django.urls import path
from . import views
from .views import PasswordsChangeView
urlpatterns = [
   path('login_user',views.login_user,name='login_user'),
   path('logout_user',views.logout_user,name='logout_user'),
   path("sign_up/",views.sign_up,name='sign_up'),
   path("<int:pk>/edit_profile_page/",views.EditProfilePageView.as_view(),name="edit_profile_page"),
   path("password_success/",views.password_success,name='password_success'),
   path("create_profile_page/<int:pk>",views.CreateProfilePageView.as_view(),name="create_profile_page"),
   path("password_change/",PasswordsChangeView.as_view(template_name='authenticate/change_password.html'),name='change_password'),
   path('<int:pk>/profile/',views.profile,name='profile'),
]