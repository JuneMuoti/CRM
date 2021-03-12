from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm

# Create your views here.

def home_page(request):
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
    
    form=LeadForm()
    if request.method =="POST":
        print("Receiving a post request")
        form=LeadForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            age=form.cleaned_data['age']
            agent=Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )

        
    context={
        "form":form
    }

    return render(request,"leads/create_lead.html",context)
