from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm

User = get_user_model()

@require_http_methods(['GET','POST'])
def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user=form.save()
                auth_login(request,user)
                return redirect('movie:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form':form,
        }
        return render(request,'user/signup.html',context=context)
    else:
        return redirect('movie:index')

@require_http_methods(['GET','POST'])
def login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request,user)
                return redirect(request.GET.get('next') or 'movie:index')
        else:
            form = AuthenticationForm()
        
        context={'form':form,}
        return render(request, 'user/login.html',context=context)
    else:
        return redirect('community:index')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('community:index')