from django.shortcuts import render
# from coming_soon_app.models import EarlyUsers
# from coming_soon_app import forms
from coming_soon_app.forms import NewUserForm


# Create your views here.

def index(request):

    return render(request, 'coming_soon_app/index.html')

def user_signup(request):
    
    form = NewUserForm()

    # request.POST
    if request.method == 'POST':
        
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            
            print('Successful Validation!')
            
            # print('Name: ', form.cleaned_data['first_name'])
            # print('Email: ', form.cleaned_data['last_name'])
            # print('Text: ', form.cleaned_data['email'])

            # Entry to the object # it generates tuple 
            # user = EarlyUsers.objects.get_or_create(first_name = form.cleaned_data['first_name'], 
            #                                         last_name = form.cleaned_data['last_name'],
            #                                         email = form.cleaned_data['email'])[0]
            
            form.save(commit=True)

            print("Data insert Successful!")

            return thank_you(request)
        else:
        # form = forms.UserForm()
        # form = forms.NewUserForm()
            
            print('Invalid Form')
    else:
        return render(request, 'coming_soon_app/user_signup.html', {'form': form})

def thank_you(request):
    return render(request, 'coming_soon_app/thank_you.html')
