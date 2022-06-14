# Generated by Django 4.0.5 on 2022-06-14 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[(None, 'Choose..'), ('small', 'Small'), ('Medium', 'Medium'), ('large', 'Large')], max_length=50)),
                ('cesit', models.CharField(choices=[('Neapolitan', 'Neapolitan'), ('Vegetarian', 'Vegetarian'), ('Margarita', 'Margarita'), ('Assorted', 'Assorted')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sauce', models.CharField(choices=[('Ketchup', 'Ketchup'), ('Mayonnaise', 'Mayonnaise'), ('Mustard', 'Mustard'), ('Chilli Sauce', 'Chilli Sauce'), ('Paprika Sauce', 'Paprika Sauce')], max_length=50)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_sauce', to='pizza.pizza')),
            ],
        ),
    ]