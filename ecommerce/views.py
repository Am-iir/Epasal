from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login ,get_user_model

from .forms import ContactForm,LoginForm,RegisterForm

def home(request):
    context={
        "title":"Home"
    }

    if request.user.is_authenticated():
        context["premium_content"]="Premium ones"     
     
    return render(request, "home.html",context)

    
def contact(request):
    contact_form= ContactForm(request.POST or None)
    context={
        "title":"Contact",
        "form":contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     print(request.POST)

    return render(request, "contact.html",context)







