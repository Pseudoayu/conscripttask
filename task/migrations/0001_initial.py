# Generated by Django 3.2.3 on 2021-10-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20)),
                ('c_name', models.CharField(max_length=30)),
                ('specialisation', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=15)),
                ('intern', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=5)),
                ('notes', models.CharField(max_length=50)),
            ],
        ),
    ]
