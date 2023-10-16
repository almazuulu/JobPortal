from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    dzName = forms.CharField(max_length=100, 
                             label='Your Name', 
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Your Name'}))
    dzEmail = forms.EmailField(label='Your Email', required=True, 
                               widget=forms.EmailInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Your Email'}))
    dzSubject = forms.CharField(max_length=100, required=True, 
                                widget=forms.Textarea(attrs={'class': 'form-control',
                                                              'placeholder': 'Subject',
                                                              'rows': '4'}),
                                label='Your message...')
    captcha = CaptchaField()