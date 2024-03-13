# To convert pages to HTML
from django.shortcuts import render

# To push information to userform and profile form
from basic_app.forms import UserForm, UserProfileInfoForm

# to create login and logout functionalities
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

# Decorator to check if user accutually login 
@login_required
def user_logout(request):
    logout(request)
    # return HttpResponseRedirect(reverse('index'))
    
    return render(request=request, template_name='basic_app/thankyou.html')

@login_required
def special(request):
    return HttpResponse("You are looking at the special page.")


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, 
                  'basic_app/registration.html', 
                  {
                      'registered': registered,
                      'user_form':user_form,
                      'profile_form': profile_form
                    })

def user_login(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, 
                            password = password)
        
        if user:
            if user.is_active:
                login(request=request, 
                      user=user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                HttpResponse("Account is not active.")

        else:
            print("Someone tried to login to account and failed.")
            print(f"Username {username} and Password {password}")
            return HttpResponse("Account details are invalid.")
        
    else:
        return render(request, 
                      'basic_app/login.html', 
                      {})



