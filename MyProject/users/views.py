from django.contrib.auth.decorators import login_required
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
        return redirect("login")
    context = {
        "form": form,
    }
    return render(request, 'users/register.html', context)


@login_required
def view_profile(request):
    return render(request, 'users/profile.html', {})
