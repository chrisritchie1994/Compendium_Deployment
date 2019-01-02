# Generated by Django 2.1.3 on 2019-01-02 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compendium_app', '0013_auto_20181202_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lesson_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('entry', models.TextField()),
                ('lesson', models.TextField()),
                ('application', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compendium_app.Journal')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('observation_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('entry', models.TextField()),
                ('observation', models.TextField()),
                ('application', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compendium_app.Journal')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
