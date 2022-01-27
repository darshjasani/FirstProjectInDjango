from django.shortcuts import render,HttpResponse
from datetime import datetime
from First.models import Contact
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from First.forms import ContactForm
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is home page")


def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is About Us page")

def contact(request):
    a = ContactForm()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name,email=email,phone=phone, date=datetime.today())
        if name != '':
            contact.save()
            messages.success(request,'Yuor form has been submiited Successfully!!')
    return render(request,'contact.html',{'form':a})
    return HttpResponse("This is Contact page")
    