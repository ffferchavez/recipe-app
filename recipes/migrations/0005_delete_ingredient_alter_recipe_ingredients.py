# Generated by Django 4.2.14 on 2024-08-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_alter_ingredient_name'),
        ('recipes', '0004_ingredient_alter_recipe_cooking_time_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='ingredients.ingredient'),
        ),
    ]
