from django.shortcuts import render,redirect
from .forms import UserRegistrationForm , ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login ,logout
from .models import Profile
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request) :
    profiles = Profile.objects.all().order_by('-created_at')
    return render(request , 'index.html', {'profiles' : profiles})


def register(request) :
    if request.method == 'POST' :
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST , request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()

            login(request,user)
            return redirect('index')
        
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request , 'register.html' , {'user_form' : user_form , 'profile_form' : profile_form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid() :
            login(request,form.get_user())
            return redirect('index')
        else :
            return render(request , 'login.html' ,{'form' : form , 'error' : 'Invalid Credentials'})
    else :
        form = AuthenticationForm()
        return render(request , 'login.html' ,{'form' : form})  


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout

    