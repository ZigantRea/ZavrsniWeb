# Generated by Django 4.0.2 on 2022-02-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Aparat", "0003_alter_napitak_vrijeme_isporuke_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="napitak",
            name="vrijeme_isporuke",
        ),
        migrations.AddField(
            model_name="narudzba",
            name="vrijeme_isporuke",
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
