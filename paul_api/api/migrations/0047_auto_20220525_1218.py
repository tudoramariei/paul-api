# Generated by Django 3.2.9 on 2022-05-25 12:18

from django.db import migrations
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.conf import settings
from django.utils import timezone
from api import models


def forwards_func(apps, schema_editor):
    Database = apps.get_model("api", "Database")
    Userprofile = apps.get_model("api", "Userprofile")

    admin_group, _ = Group.objects.get_or_create(name="admin")
    if not Database.objects.exists():
        Database.objects.create(name="PAUL")

    # User = get_user_model()
    if not User.objects.exists():
        admin = User.objects.create(
            username=settings.DJANGO_ADMIN_USERNAME,
            email=settings.DJANGO_ADMIN_EMAIL,
            last_login=timezone.now(),
            is_superuser=True,
            is_staff=True
        )
        admin.set_password(settings.DJANGO_ADMIN_PASSWORD)
        admin.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_auto_20211206_1958'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]


