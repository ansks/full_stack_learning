from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    # Hidden Fields, these fields will be hidden from the user. It will be available in html but hidden from the user. 
    


