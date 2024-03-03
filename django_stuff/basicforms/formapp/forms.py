from django import forms
from django.core import validators

# Adding a custom validation and using django validator function.

def check_for_z(value):

    if value[0].lower() != 'a':
        raise forms.ValidationError("Name should start with 'a'. ")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    vrfyemail = forms.EmailField(label='Please reenter your email.')
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    # def clean_botcather(self):
    #     botcather = self.cleaned_data['botcatcher']

    #     if len(botcather) > 0:
    #         raise forms.ValidationError('You are a bot.')

    #     return botcather


    def clean(self):
        all_clean_data = super().clean()

        email = all_clean_data['email']
        vrfyemail = all_clean_data['vrfyemail']

        if email != vrfyemail:
            raise forms.ValidationError('Your Emails dont match. Please check. ')

