# Generated by Django 3.1.2 on 2020-10-26 12:26

from django.conf import settings
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0037_auto_20201026_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('data_column_function', models.CharField(choices=[('Count', 'Count'), ('Sum', 'Sum'), ('Min', 'Min'), ('Max', 'Max'), ('Avg', 'Average'), ('StdDev', 'Standard Deviation')], default='Count', max_length=10)),
                ('filters', models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_edit_date', models.DateTimeField(blank=True, null=True)),
                ('data_column', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cards_column_fields', to='api.tablecolumn')),
                ('last_edit_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_card_edits', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.table')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
