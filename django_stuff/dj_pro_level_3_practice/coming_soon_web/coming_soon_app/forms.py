from django import forms
from django.core.exceptions import ValidationError
from coming_soon_app.models import EarlyUsers

# Create your models here.
# class UserForm(forms.Form):
#     ''' 
#     Defining all the attributes for the user

#     first_name -- first name
#     last_name -- last_name
#     email -- email 
#     verify_email -- verify email 
#     botcatcher -- botcatcher (Hidden Input)
#     '''

#     first_name = forms.CharField(label = 'Your first name: ', max_length=128)
#     last_name = forms.CharField(label = 'Your last name: ', max_length=128)
#     email = forms.EmailField(label='Your email', max_length=264)
#     verify_email = forms.EmailField(label='Verify your email: ', max_length=264)
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
    
#     # Cleaning the data for validation error

#     def clean(self):
#         '''
#         Cleaning the form and checking for mistakes and mismatch.
#         '''
#         cleaned_data = super().clean()
#         email = cleaned_data["email"]
#         verify_email = cleaned_data["verify_email"]
#         botcatcher = cleaned_data["botcatcher"]

#         if email != verify_email:
#             raise ValidationError('Emails do not match!')
        
#         if len(botcatcher) > 0:
#             raise ValidationError("Gotcha Bot!")


class NewUserForm(forms.ModelForm):

    class Meta():
        
        model = EarlyUsers
        fields =  '__all__'




