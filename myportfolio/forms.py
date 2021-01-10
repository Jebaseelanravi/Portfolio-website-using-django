from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100,widget=forms.TextInput(attrs={'placeholder':'Your '
                                                                                                              'Name'}))
    email = forms.EmailField(label='Your Email',widget=forms.TextInput(attrs={'placeholder':'example@example.com'}))
    subject = forms.CharField(label='Subject', max_length=100,widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your message'}))