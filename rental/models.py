from datetime import date

from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'#{self.id:<3}  {self.first_name} {self.last_name}'


class BicycleType(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return f'{self.name}'


class FrameMaterial(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return f'{self.name}'


class RentalRate(models.Model):
    daily_rate = models.IntegerField()
    img_path = models.CharField(max_length=100, default='/rental/images/canyon.png')
    bicycle_type = models.ForeignKey(BicycleType, on_delete=models.CASCADE)
    frame_material = models.ForeignKey(FrameMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return f'The Daily Rate for a {str(self.frame_material)} {str(self.bicycle_type)}: ${self.daily_rate}'


class Bicycle(models.Model):
    real_cost = models.IntegerField()
    date_created = models.DateField()
    bicycle_type = models.ForeignKey(BicycleType, on_delete=models.CASCADE)
    frame_material = models.ForeignKey(FrameMaterial, on_delete=models.CASCADE)
    img_path = models.CharField(max_length=100, default='/rental/images/canyon.png')

    @property
    def rate(self):
        "Fetches the daily rate for the bicycle"
        return RentalRate.objects.get(
            bicycle_type__id=self.bicycle_type.id,
            frame_material__id=self.frame_material.id).daily_rate

    def __repr__(self):
        return f'A ${self.real_cost} {str(self.frame_material)} \
{str(self.bicycle_type)}, created on {self.date_created}.'

    def __str__(self):
        return f'{self.frame_material} {self.bicycle_type}'

    def check_availability(self, start: date, end):
        if not end:
            end = date.today()
        # print(f"start: {str(start)}   End {str(end)}")
        rentals = Rental.objects.filter(bicycle=self)
        for rental_period in rentals:
            if not rental_period.return_date:
                rental_period.return_date = date.today()
            # print(f"Existing rental from {str(rental_period.start_date)} to {str(rental_period.return_date)}")
            if (rental_period.start_date <= start <= rental_period.return_date
                    or rental_period.start_date <= end <= rental_period.return_date):
                return False
            if start < rental_period.start_date and end > rental_period.return_date:
                return False

        return True


class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)

    @property
    def duration(self):
        if self.return_date:
            return (self.return_date - self.start_date).days

        return (date.today() - self.start_date).days

    @property
    def total_cost(self):
        return self.duration * self.bicycle.rate
