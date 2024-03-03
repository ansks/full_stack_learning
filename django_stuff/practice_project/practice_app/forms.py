from django import forms


class UserInfo(forms.Form):

    name = forms.CharField(label="Your name", max_length=264)
    email = forms.CharField(label='Your email', max_length=264)
    password = forms.CharField(label = 'Your password', max_length=264)
    retype_password = forms.CharField(label = 'Retype your password', max_length=264)

    def clean(self):

        clean_data =super().changed_data()
        password = clean_data['password']
        retype_password = clean_data['retype_password']

        if password != retype_password:
            raise('Password does not match.')



        
        


