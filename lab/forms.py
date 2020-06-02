from django import forms
from lab.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
	fields = ['name', 'email', 'subject', 'message']
        
