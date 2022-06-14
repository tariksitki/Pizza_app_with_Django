from unicodedata import name
from django.shortcuts import render
from .forms import PizzaForm

# Create your views here.


def home(request):
    return render(request, "pizza/home.html")



def order(request):
    form = PizzaForm()

    context = {
        "form" : form
    }

    return render(request, "pizza/order.html", context)