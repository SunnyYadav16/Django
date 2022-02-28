from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f"Welcome {username}. Your account has been created!")
        return redirect("food:index")
    context = {
        "form": form,
    }
    return render(request, 'users/register.html', context)


def view_profile(request):
    user = User.objects.get(username="Sunny")
    context = {
        "user": user,
    }
    return render(request, 'users/profile.html', context)
