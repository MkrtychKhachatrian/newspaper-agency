# Generated by Django 4.2 on 2023-05-16 16:54

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):
    dependencies = [
        ("agency", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newspaper",
            name="content",
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
