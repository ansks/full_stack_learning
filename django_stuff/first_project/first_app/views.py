from django.shortcuts import render
from django.http import HttpResponse

from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):

    # Step 1: Simple Response
    # return HttpResponse("<em> Hello world!! </em>")

    # Step 2: Dictionary defined and providing value:
    # test_dict = {'define_variable': 'This is a test variable coming from first app views!'}
    # return render(request, 'first_app/index.html', context=test_dict)

    # Reading data from model
    webpage_records = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_records}

    return render(request, 'first_app/index.html', context=date_dict)




    
