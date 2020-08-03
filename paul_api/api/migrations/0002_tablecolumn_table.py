# Generated by Django 3.1rc1 on 2020-07-28 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tablecolumn",
            name="table",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="columns",
                to="api.table",
            ),
            preserve_default=False,
        ),
    ]