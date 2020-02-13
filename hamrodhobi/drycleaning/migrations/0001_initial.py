# Generated by Django 3.0.1 on 2020-02-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, verbose_name=100)),
                ('phone', models.BigIntegerField(verbose_name=100)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('clothtype', models.CharField(max_length=50)),
                ('choose_service', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
