from django.shortcuts import redirect, render
from posts.models import Post, Vote
from .forms import PostForm, PostUpdateForm


def add_new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/posts')
    else:
        form = PostForm()
    context={
        'form': form
    }
    return render(request,'addpost.html', context)


def list_posts(request):
    posts = Post.objects.all().order_by('date')[::-1] 
     #[::-1] had been aded becouse '-date' paramether caused bug in same-date objects
    context={
        'posts': posts,
    }
    return render(request,'posts.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post':post,
    }
    return render(request, 'post_detail.html', context)

def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'/post_detail/{pk}')
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post_edit.html', context)

def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/posts')

    return render(request, 'post_delete.html')
