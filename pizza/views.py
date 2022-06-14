from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .forms import PizzaForm, SauceForm

# Create your views here.


def home(request):
    return render(request, "pizza/home.html")



def order(request):
    form = PizzaForm()

    context = {
        "form" : form
    }

    return render(request, "pizza/order.html", context)






def numberOfPizza(request):
    # print(int(request.GET.get("number")))
    pizzaForm = PizzaForm()
    sauceForm = SauceForm()
    number_pizza = int(request.GET.get("number"))
    mylist = [1 for i in range(number_pizza)]
    print(mylist)


    context = {
        "mylist" : mylist,
        "pizzaForm" : pizzaForm,
        "sauceForm" : sauceForm

    }

    return render(request, "pizza/pizzas.html", context)