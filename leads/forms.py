from django import forms

class LeadForm(forms.Form):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    age=forms.IntegerField(min_value=0)