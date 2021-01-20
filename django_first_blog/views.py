from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def home_page(request):
    title = "main page"
    some_list = ["alpha", "thingy", "whatever"]
    return render(request, 'index.html', {"title": title, "data": some_list})


def about_page(request):
    return render(request, 'about.html', {"title": "About Us"})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()  # empties out form upon successful send
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(request, 'form.html', context)
