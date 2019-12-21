from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from rental.forms import AddRentalForm, AddCustomerForm
from rental.models import Customer, Rental, Bicycle, RentalRate


def index(request):
    return render(request, 'index.html')


def customers(request):
    customer_list = Customer.objects.all().order_by('last_name')
    paginator = Paginator(customer_list, 15)
    page = request.GET.get('page')
    customers = paginator.get_page(page)
    return render(request, 'customers.html', {
        'paginator': paginator,
        'page_obj': customers})


def view_customer(request, cust_id):
    try:
        customer = Customer.objects.get(id=cust_id)
    except Customer.DoesNotExist:
        return redirect('customers')

    rentals = Rental.objects.filter(customer=customer).order_by('-return_date')

    return render(request, 'customer.html', {
        'customer': customer,
        'rentals': rentals})


def view_by_type(request, bike_type):
    bike_list = Bicycle.objects.filter(bicycle_type__name=bike_type).order_by('id')
    if not bike_list:
        return redirect('index')

    paginator = Paginator(bike_list, 9)
    page = request.GET.get('page')
    bikes = paginator.get_page(page)
    return render(request, 'view_bikes.html', {
        'bike_type': bike_type.capitalize(),
        'paginator': paginator,
        'page_obj': bikes
    })

def view_bike_types(request):
    bike_type_list = RentalRate.objects.order_by(
        'bicycle_type', 'frame_material'
    )

    return render(request, 'bike_types.html', {
        'type_list': bike_type_list
    })

def view_all_bikes(request):
    bike_list = Bicycle.objects.order_by('id')
    paginator = Paginator(bike_list, 12)
    page = request.GET.get('page')
    bikes = paginator.get_page(page)
    return render(request, 'view_bikes.html', {
        'bike_type': 'Bike',
        'paginator': paginator,
        'page_obj': bikes
    })


def bike_page(request, bike_id):
    try:
        current_bike = Bicycle.objects.get(id=bike_id)
    except Bicycle.DoesNotExist:
        return redirect('view-all-bikes')

    rental_history = Rental.objects.filter(
        bicycle=current_bike).order_by('-start_date')
    return render(request, 'view_bike.html', {
        'bike': current_bike,
        'rentals': rental_history
    })


def add_rental(request, bike_id):
    try:
        bike = Bicycle.objects.get(id=bike_id)
    except Bicycle.DoesNotExist:
        return redirect('view-all-bikes')

    if request.method == 'POST':
        form = AddRentalForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            start = form.cleaned_data['start_date']
            finish = form.cleaned_data['return_date']

            try:
                if not bike.check_availability(start, finish):
                    raise ValidationError ('Sorry, the bike is not available during those dates.')
            except ValidationError:
                print('bike not available during those dates')
                return redirect('view-bike', bike_id)

            new_rental = Rental(bicycle=bike, **form.cleaned_data)
            new_rental.save()
            print(new_rental)
            return redirect('index')

    else:
        form = AddRentalForm()

    return render(request, 'add_rental.html', {
        'form': form,
        'bike': bike
    })

def add_customer(request):
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            new_customer = Customer(**form.cleaned_data)
            new_customer.save()
            print(new_customer)
            return redirect('view-single-customer', new_customer.id)

    else:
        form = AddCustomerForm()

    return render(request, 'new_customer.html', {'form': form})

def view_all_rentals(request):
    rental_list = Rental.objects.order_by('-return_date')
    paginator = Paginator(rental_list, 15)
    page = request.GET.get('page')
    rentals = paginator.get_page(page)
    return render(request, 'view_rentals.html', {
        'paginator': paginator,
        'page_obj': rentals
    })
