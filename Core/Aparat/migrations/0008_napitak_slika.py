# Generated by Django 4.0.2 on 2022-02-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Aparat", "0007_narudzba_adresa_narudzba_grad"),
    ]

    operations = [
        migrations.AddField(
            model_name="napitak",
            name="slika",
            field=models.ImageField(default="default_drink.jpg", upload_to=""),
        ),
    ]
