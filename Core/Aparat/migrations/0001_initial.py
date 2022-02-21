# Generated by Django 4.0.2 on 2022-02-19 13:30

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dodaci",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("naziv", models.CharField(max_length=255)),
                ("cijena", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name="Napitak",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vrsta_napitka", models.CharField(max_length=255)),
                ("cijena", models.DecimalField(decimal_places=2, max_digits=6)),
                ("toplo_hladno", models.BooleanField(default=True)),
                ("vrijeme_isporuke", models.TimeField()),
                ("dodatak", models.ManyToManyField(blank=True, to="Aparat.Dodaci")),
            ],
        ),
        migrations.CreateModel(
            name="Narudzba",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("broj_narudzbe", models.CharField(max_length=255)),
                ("vrijeme_kupnje", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Salica",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "boja",
                    colorfield.fields.ColorField(
                        default="#FF0000", image_field=None, max_length=18, samples=None
                    ),
                ),
                ("materijal", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Stavka",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("kolicina", models.IntegerField()),
                (
                    "cijena",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
                ),
                (
                    "napitak",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Aparat.napitak"
                    ),
                ),
                (
                    "narudzba",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stavke",
                        to="Aparat.narudzba",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="napitak",
            name="salica",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Aparat.salica"
            ),
        ),
        migrations.CreateModel(
            name="DodatakNapitak",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dodatak",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Aparat.dodaci"
                    ),
                ),
                (
                    "napitak",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Aparat.napitak"
                    ),
                ),
            ],
        ),
    ]