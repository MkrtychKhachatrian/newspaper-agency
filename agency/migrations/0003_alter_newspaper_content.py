# Generated by Django 4.2 on 2023-05-16 16:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("agency", "0002_alter_newspaper_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newspaper",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
