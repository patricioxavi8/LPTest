# Generated by Django 2.1.7 on 2019-08-16 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=100)),
                ('url_imagen', models.CharField(max_length=100)),
            ],
        ),
    ]
