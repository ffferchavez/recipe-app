# Generated by Django 4.2.14 on 2024-08-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='preparation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
