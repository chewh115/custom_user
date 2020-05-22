from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from custom_user.settings import AUTH_USER_MODEL
from customize.forms import LoginForm, SignupForm
from customize.models import MyUser

# Create your views here.
def index(request):
    auth_stuff = AUTH_USER_MODEL
    if request.user.is_authenticated:
        user_info = request.user
        return render(request, 'index.html', {'user_info': user_info, 'auth_stuff': auth_stuff})
    return redirect("/login/")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_info = form.cleaned_data
            user = authenticate(
                request,
                username = user_info['username'],
                password = user_info['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user_info = form.cleaned_data
            MyUser.objects.create(
                username = user_info['username'],
                display_name = user_info['display_name'],
                homepage = user_info['homepage'],
                age = user_info['age']
            )
            user = MyUser.objects.last()
            user.set_password(user_info['password'])
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))