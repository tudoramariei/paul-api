# Generated by Django 3.1 on 2020-08-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_auto_20200827_0722"),
    ]

    operations = [
        migrations.AddField(
            model_name="csvimport",
            name="delimiter",
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name="csvfieldmap",
            name="field_format",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="tablecolumn",
            name="display_name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
