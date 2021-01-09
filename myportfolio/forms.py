from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(widget=forms.Textarea)