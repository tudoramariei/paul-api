# Generated by Django 3.1.2 on 2020-10-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugin_woocommerce', '0004_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='In progress', max_length=20),
        ),
    ]