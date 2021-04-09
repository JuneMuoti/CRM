from django import forms
from .models import Lead,User
from django.contrib.auth.forms import UserCreationForm,UsernameField

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class LeadModelForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = ("first_name",
                "last_name",
                "age",
                "source",
                "agent"
                 )

class LeadForm(forms.Form):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    age=forms.IntegerField(min_value=0)