from django.db import models

# Create your models here.

# class Size(models.Model):
#     title = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title






class Pizza(models.Model):
    SIZE = ((None, 'Choose..'),
        ('small', 'Small'),
        ('Medium', 'Medium'),
        ('large', 'Large'),
    )

    PIZZA = (
        ('Neapolitan', 'Neapolitan'),
        ('Vegetarian', 'Vegetarian'),
        ('Margarita', 'Margarita'),
        ('Assorted', 'Assorted'),
    )
    

    size = models.CharField(max_length=50, choices=SIZE)
    cesit = models.CharField(max_length=50, choices=PIZZA)





class Sauce(models.Model):
    # SAUCE = (('Ketchup', 'Ketchup'),
    #     ('Ketchup', 'Mayonnaise'),
    #     ('Mustard', 'Mustard'),
    #     ('Chilli Sauce', 'Chilli Sauce'),
    #     ('Paprika Sauce', 'Paprika Sauce')
    # )
    Ketchup = models.BooleanField(default=False)
    Mayonnaise = models.BooleanField(default=False)
    Mustard = models.BooleanField(default=False)
    ChilliSauce = models.BooleanField(default=False)
    PaprikaSauce = models.BooleanField(default=False)


    # sauce = models.CharField(max_length=50, choices=SAUCE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="pizza_sauce")

