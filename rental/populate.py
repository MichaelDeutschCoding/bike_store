from faker import Faker
from rental.models import Customer, RentalRate, FrameMaterial, Bicycle, BicycleType, Rental
from random import choice, randrange
from datetime import timedelta, date

faker = Faker()


def create_users(num):
    for _ in range(num):
        first = faker.first_name()
        last = faker.last_name()
        email = faker.email()
        phone = faker.msisdn()

        cust = Customer(first_name=first,
                        last_name=last,
                        email=email,
                        phone_number=phone)

        cust.save()

    print(f'Successfully added {num} Customers to the database.')


def create_bicycle(num):
    types = BicycleType.objects.all()
    materials = FrameMaterial.objects.all()

    for _ in range(num):
        created = faker.date_this_decade()
        bike = Bicycle(
            real_cost = randrange(500, 2000),
            date_created = created,
            bicycle_type = choice(types),
            frame_material = choice(materials)
        )

        bike.save()

    print(f'Successfully added {num} Bicycles to the database.')


def create_rental(num):
    added = 0
    bikes = Bicycle.objects.all()
    customers = Customer.objects.all()

    for _ in range(num):
        bike = choice(bikes)
        # print(bike, bike.id)

        start_date = faker.date_between_dates(
            date_start=bike.date_created
        )

        if (date.today() - start_date).days < 30:
            return_date = None
        else:
            due_by = start_date + timedelta(days=30)
            return_date = faker.date_between_dates(
                date_start=start_date,
                date_end=due_by
            )

        if not bike.check_availability(start_date, return_date):
            continue

        rental = Rental(
            start_date=start_date,
            return_date=return_date,
            customer=choice(customers),
            bicycle=bike
        )
        added +=1
        rental.save()

    print(f"Successfully added {added} rentals!")

