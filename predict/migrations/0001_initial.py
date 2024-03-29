# Generated by Django 4.2 on 2023-04-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newuser',
            fields=[
                ('my_id', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=80)),
                ('fname', models.CharField(max_length=89)),
                ('lname', models.CharField(max_length=88)),
                ('email', models.EmailField(max_length=90)),
                ('pass1', models.CharField(max_length=90)),
                ('pass2', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('symptom1', models.CharField(max_length=30)),
                ('symptom2', models.CharField(blank=True, max_length=30)),
                ('symptom3', models.CharField(blank=True, max_length=30)),
                ('symptom4', models.CharField(blank=True, max_length=30)),
                ('symptom5', models.CharField(blank=True, max_length=30)),
                ('disease', models.CharField(max_length=30)),
                ('consultDoctor', models.CharField(max_length=30)),
            ],
        ),
    ]
