# Generated by Django 3.0.1 on 2019-12-19 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=31)),
                ('last_name', models.CharField(max_length=31)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RentalRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VehicleSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_cost', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('license_plate', models.IntegerField()),
                ('rental_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.RentalRate')),
                ('vehicle_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.VehicleSize')),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.VehicleType')),
            ],
        ),
        migrations.AddField(
            model_name='rentalrate',
            name='vehicle_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.VehicleSize'),
        ),
        migrations.AddField(
            model_name='rentalrate',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.VehicleType'),
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('return_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Customer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Vehicle')),
            ],
        ),
    ]
