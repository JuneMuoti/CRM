from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm
from django.contrib import messages
# Create your views here.

def lead_list(request):
    leads=Lead.objects.all()
    context={
       
       "leads":leads
    }
    return render(request,"leads/home_page.html",context)



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
