# Generated by Django 5.0.2 on 2024-02-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students_model',
            fields=[
                ('student_Name', models.CharField(max_length=264)),
                ('student_Roll', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('student_domain', models.CharField(max_length=264)),
            ],
        ),
    ]
