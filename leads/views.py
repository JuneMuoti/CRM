from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm,CustomUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.


class SignUpView(CreateView):
    template_name="registration/signup.html"
    form_class=CustomUserForm

    def get_success_url(self):
        return reverse("login")


class HomePageView(TemplateView):
    template_name="home_page.html"

class LeadListView(ListView):
    queryset=Lead.objects.all()
    context_object_name="leads"
    template_name = 'leads/lead_list.html'
class LeadDetailView(DetailView):
    queryset=Lead.objects.all()
    context_object_name="lead"
    template_name="leads/lead_detail.html"

class LeadCreateView(CreateView):
    template_name="leads/create_lead.html"
    form_class=LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")



class LeadUpdateView(UpdateView):
    template_name="leads/update_lead.html"
    form_class=LeadModelForm
    queryset=Lead.objects.all()
class LeadDeleteView(DeleteView):
    template_name="leads/delete_lead.html"
    queryset=Lead.objects.all()
    def get_success_url(self):
        return reverse("leads:lead-list")




def home_page(request):
    return render(request,"home_page.html")



def lead_list(request):
    leads=Lead.objects.all()
    context={
       
       "leads":leads
    }
    return render(request,"leads/lead_list.html",context)



def lead_detail(request,pk):
    
    lead=Lead.objects.get(id=pk)
    print(lead)
    context={
        "lead":lead
    }
    return render(request,"leads/lead_detail.html",context)

def lead_create(request):
    
    form=LeadModelForm()
    if request.method =="POST":
        print("Receiving a post request")
        form=LeadModelForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            
            form.save()
            messages.success(request, 'Lead has been  created!')
            # return redirect("/leads/")

        
    context={
        "form":form
    }

    return render(request,"leads/create_lead.html",context)
def lead_update(request,pk):
    lead=Lead.objects.get(id=pk)
    form=LeadModelForm(instance=lead)
    if request.method =="POST":
        print("Receiving a post request")
        form=LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            
            form.save()
            messages.success(request, 'Lead has been  updated!')
            # return redirect("/leads/")
    context={
         "form":form,
         "lead":lead
     }
    return render(request,"leads/update_lead.html",context)
def lead_delete(request,pk):
    lead=Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads/")
# def lead_update(request,pk):
#     lead=Lead.objects.get(id=pk)
#     form=LeadForm()
#     if request.method== "POST":
#         form=LeadForm(request.POST)
#         if form.is_valid():

#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']

#             lead.first_name=first_name
#             lead.last_name=last_name
#             lead.age=age
#             lead.save()
#             messages.success(request,"Lead has been updated!")
#             return redirect("/leads/")


#     context={
#         "form":form,
#         "lead":lead
#     }
#     return render(request,"leads/update_lead.html",context)


