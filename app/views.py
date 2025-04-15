from django.shortcuts import render,redirect


def About(request):
    return render(request, "About.html")
def Contact(request):
    return render(request, "Contact.html")
def Privacy(request):
    return render(request, "Privacy.html")
def Terms(request):
    return render(request, "Terms.html")

from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash password
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('home')
        messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')
