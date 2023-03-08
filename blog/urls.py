from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('about/', about),
    path('', include('posts.urls')),
    path('users/',include('users.urls'))
]

urlpatterns += staticfiles_urlpatterns()
