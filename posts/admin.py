from django.contrib import admin
from .models import Post, Vote

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content']
    pass

@admin.register(Vote)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['id','reason']
    pass

# admin.site.register(Post)
# admin.site.register(Vote)
