# Generated by Django 4.0.5 on 2022-06-30 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_blogmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(upload_to='log'),
        ),
    ]
