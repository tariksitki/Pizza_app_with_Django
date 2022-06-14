from django.db import models

# Create your models here.

class Size(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title





class Pizza(models.Model):
    topping1 = models.CharField(max_length=50)
    topping2 = models.CharField(max_length=50)
    size = models.ForeignKey(Size, related_name="pizza_size", on_delete=models.CASCADE)