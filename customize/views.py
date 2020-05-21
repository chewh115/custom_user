from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from customize.forms import LoginForm, SignupForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')


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
    if request == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user_info = form.cleaned_data
            MyUser.objects.create(
                username = user_info['username'],
                password = user_info['password'],
                display_name = user_info['display_name'],
                homepage = user_info['homepage'],
                age = user_info['age']
            )
            new_user = MyUser.objects.last()
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))
        return render(request, 'signup.html', {'form': form})
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))