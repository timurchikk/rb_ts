# Generated by Django 4.0.4 on 2022-05-31 05:35

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
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50, verbose_name='Deparment')),
            ],
            options={
                'verbose_name': 'Depatrment',
                'verbose_name_plural': 'Depatrments',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100, verbose_name='Role')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='First name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Last name')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.department', verbose_name='Department')),
                ('residental_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.address', verbose_name='Address')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.role', verbose_name='Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
