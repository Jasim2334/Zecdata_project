# Generated by Django 4.1.5 on 2023-01-16 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HabitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit1', models.CharField(blank=True, max_length=70)),
                ('habit2', models.CharField(blank=True, max_length=70)),
                ('habit3', models.CharField(blank=True, max_length=70)),
                ('habit4', models.CharField(blank=True, max_length=70)),
                ('habit5', models.CharField(blank=True, max_length=70)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
