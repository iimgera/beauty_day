# Generated by Django 4.1.7 on 2023-04-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("otzyv", "0002_article_articleimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="is_publish",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="review",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
