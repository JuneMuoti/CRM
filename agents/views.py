from django.shortcuts import render

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentsModelForm


# Create your views here.

class AgentsListView(LoginRequiredMixin,generic.ListView):

    context_object_name='agents'
    template_name="agents/agents_list.html"
    form_class=None

    def get_queryset(self):
        return Agent.objects.all()

class AgentsCreateView(LoginRequiredMixin,generic.CreateView):
    template_name="agents/create_agent.html"
    form_class=AgentsModelForm
    def get_success_url(self):
        return reverse("agents:agent_list.html")


    def form_valid(self,form):
        agent=form.save(commit=False)
        # commit=false means don't commit to the database first
        agent.organization=self.request.user.userprofile
        agent.save()
        return super(AgentsCreateView,self).form_valid(form)




    


