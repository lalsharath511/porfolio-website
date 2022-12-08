# Generated by Django 4.1.3 on 2022-12-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_delete_blogs"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blogs",
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
                ("title", models.CharField(max_length=80)),
                ("description", models.TextField()),
                ("joburl", models.TextField()),
                ("authname", models.CharField(max_length=20)),
                ("img", models.ImageField(blank=True, null=True, upload_to="blog")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]