# Generated by Django 2.0.7 on 2018-07-11 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCPal', '0009_gpu'),
    ]

    operations = [
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hdd_name', models.CharField(max_length=200)),
                ('hdd_price', models.CharField(max_length=200)),
                ('hdd_cap', models.CharField(max_length=200)),
            ],
        ),
    ]
