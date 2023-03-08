from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_view
from users.views import *



urlpatterns = [
    path('sign_up/', sign_up),
    path('profile/', profile),
    path('result/', result),
    path('login/', auth_view.LoginView.as_view(template_name="login.html"), name ='user-login'),
    path('logout/',auth_view.LogoutView.as_view(template_name="logout.html"), name ='user-logout'),
]

urlpatterns += staticfiles_urlpatterns()
