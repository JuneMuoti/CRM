from leads.models import Agent

from django import forms


class  AgentsModelForm(forms.ModelForm):
    
    class Meta:
        model = Agent
        fields = ("user",)
