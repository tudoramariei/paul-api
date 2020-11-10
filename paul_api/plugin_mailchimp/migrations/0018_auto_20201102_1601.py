# Generated by Django 3.1.2 on 2020-11-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugin_mailchimp', '0017_task_periodic_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskresult',
            old_name='date',
            new_name='date_start',
        ),
        migrations.AddField(
            model_name='taskresult',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taskresult',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
    ]