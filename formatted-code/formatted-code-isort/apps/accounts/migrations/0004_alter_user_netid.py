# Generated by Django 5.1.1 on 2024-09-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_user_is_staff_alter_user_is_superuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="netid",
            field=models.CharField(max_length=30, unique=True, verbose_name="net id"),
        ),
    ]
