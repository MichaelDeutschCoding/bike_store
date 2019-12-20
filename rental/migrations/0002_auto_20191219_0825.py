# Generated by Django 3.0.1 on 2019-12-19 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VehicleType',
            new_name='BicycleType',
        ),
        migrations.RenameModel(
            old_name='VehicleSize',
            new_name='FrameMaterial',
        ),
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_cost', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('rental_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.RentalRate')),
                ('vehicle_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.FrameMaterial')),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.BicycleType')),
            ],
        ),
        migrations.AlterField(
            model_name='rental',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Bicycle'),
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
