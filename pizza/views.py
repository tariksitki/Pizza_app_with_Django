from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
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
    
    if request.method == "POST":
        pizzaForm = PizzaForm(request.POST)
        sauceForm = SauceForm(request.POST)
        if pizzaForm.is_valid() and sauceForm.is_valid():
            pizza = pizzaForm.save()
            sauce = sauceForm.save(commit = False)
            sauce.pizza = pizza 
            sauce.save()
            return redirect("home")


    context = {
        "mylist" : mylist,
        "pizzaForm" : pizzaForm,
        "sauceForm" : sauceForm

    }

    return render(request, "pizza/pizzas.html", context)