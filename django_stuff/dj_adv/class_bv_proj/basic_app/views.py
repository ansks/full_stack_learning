from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, 
                                  DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.http import HttpResponse
from . import models

# Method 1
# Create your views here.
# def index(request):
#     return render(request, 'basic_app/index.html')

# Method 2
# class CBView(View):

#     def get(self, request):
#         return HttpResponse('Class based view is being tested.')

# Using Template View
class IndexView(TemplateView):

    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        
        context_data = super().get_context_data(**kwargs)
        context_data['injecting_data'] = "\nPam Pam pa pa Pam!!"

        return context_data

# List and Detail view
class SchoolListview(ListView):
    # By default it gives context list as <lowercase model name + '_' + list> but 
    # name can be changed using context_object_name data variable. 
    context_object_name = "schools"
    model = models.School
    
class SchoolDetailView(DetailView):
    
    context_object_name = 'school_detail'
    model = models.School
    
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):

    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):

    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):

    model = models.School
    success_url = reverse_lazy("basic_app:list_view")




