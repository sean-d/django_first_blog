from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    title = "main page"
    some_list = ["alpha", "thingy", "whatever"]
    return render(request, 'index.html', {"title": title, "data": some_list})


def about_page(request):
    return render(request, 'about.html', {"title": "About Us"})


def contact_page(request):
    return render(request, 'contact.html', {"title": "Contact Us"})
