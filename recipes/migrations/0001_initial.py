# Generated by Django 4.2.14 on 2024-08-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cooking_time', models.IntegerField()),
                ('ingredients', models.ManyToManyField(to='ingredients.ingredient')),
            ],
        ),
    ]
