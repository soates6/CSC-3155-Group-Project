# Generated by Django 5.1.2 on 2024-12-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0004_remove_room_host_remove_room_participants_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('qualifications', models.TextField()),
                ('salary', models.CharField(blank=True, max_length=50, null=True)),
                ('about_company', models.TextField()),
                ('offers', models.TextField()),
            ],
        ),
    ]