from django import forms
from .models import *
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,label='Name')
    email=forms.EmailField(label='Email')
    phone=forms.CharField(label='Phone')
    message=forms.CharField(widget=forms.Textarea,label='Message')

class studentForm(forms.ModelForm):
    class Meta:
        model=student
        fields=['name','phone','age']