# Generated by Django 5.0.2 on 2024-03-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bnc_web", "0022_alter_userprofile_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="date_of_birth",
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="instagram_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
