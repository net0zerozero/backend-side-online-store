# Generated by Django 4.2 on 2023-04-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quickstart", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdata",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="userdata",
            name="date_joined",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="userdata",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="userdata",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="userdata",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
