from django.shortcuts import render, HttpResponse
from practice_app.models import userlist
from .forms import UserInfo


# Create your views here.
def help(request):
    # return HttpResponse('<strong> Your practice app is working. </strong>')

    practice_dict = {
        'get_python_variable': 'This is me coming from practice app. '
    }

    return render(request, 
                  'practice_app/help.html',
                  context=practice_dict)


def user_list(request):
    '''
    This function will read data from the models.py and display it on front end. 
    '''
    # userlist.objects.order_by('first_name')

    practice_dict = {
        'userInfo': userlist.objects.all()
    }

    return render(request, 
                  'practice_app/userlist.html',
                  context=practice_dict)

def get_user_details(request):
    '''
    This function will collect user details from front end. 
    '''
    form = UserInfo()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = UserInfo(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

        # if a GET (or any other method) we'll create a blank form
        else:
            form = UserInfo()

    return render(request, "practice_app/help.html", {"form": form})

