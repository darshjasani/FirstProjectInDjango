from dataclasses import field
from unittest.util import _MAX_LENGTH
from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(label="Enter the Username :",max_length=256)
    email = forms.EmailField(label="Enter the Email Id :",max_length=122)
    phone = forms.CharField(label="Enter the  phone number :",max_length=10)
