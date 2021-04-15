from django.shortcuts import render

from django.views.generic  import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent


# Create your views here.

class AgentsListView(LoginRequiredMixin,ListView):

    context_object_name='agents'
    template_name="agents/agents_list.html"
    def get_queryset(self):
        return Agent.objects.all()
    


