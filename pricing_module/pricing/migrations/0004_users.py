# Generated by Django 3.2.4 on 2023-03-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0003_delete_servicespricing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('dept', models.CharField(max_length=50)),
            ],
        ),
    ]
