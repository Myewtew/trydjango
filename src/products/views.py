from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
     #return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def social_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my_number": 123
    }
    #return HttpResponse("<h1>Social View</h1>")
    return render(request, "social.html", {})
