# Generated by Django 3.0.1 on 2019-12-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0006_auto_20191219_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycle',
            name='img_path',
            field=models.CharField(default='/rental/images/canyon.png', max_length=100),
        ),
    ]
