from unicodedata import name
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "pizza/home.html")