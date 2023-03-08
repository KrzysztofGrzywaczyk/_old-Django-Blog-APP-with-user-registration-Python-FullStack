from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/login/')
    else:
        form = SignUpForm()

    form = SignUpForm()
    context = {
        'form':form
    }
    return render(request, 'sign_up.html', context)

def result(request):
    msg = "User successfully created"
    context={
        'msg': msg
        }
    return render(request, 'result.html', context)

def profile(request):
    return render(request, 'profile.html')
    
