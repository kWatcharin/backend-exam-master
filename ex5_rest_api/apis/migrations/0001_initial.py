# Generated by Django 5.0.4 on 2024-09-08 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('abbreviated_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField()),
                ('section', models.CharField(max_length=20)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='apis.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='apis.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('classroom', models.ManyToManyField(related_name='teachers', to='apis.classroom')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='apis.school')),
            ],
        ),
    ]
