from django.core.paginator import Paginator
from django.shortcuts import render, redirect

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


def customer(request, cust_id):
    try:
        customer = Customer.objects.get(id=cust_id)
    except Customer.DoesNotExist:
        return redirect('customers')

    rentals = Rental.objects.filter(customer=customer).order_by('-return_date')

    return render(request, 'customer.html', {
        'customer': customer,
        'rentals': rentals})


def view_by_type(request, bike_type):
    bike_list = Bicycle.objects.filter(bicycle_type__name=bike_type)
    if not bike_list:
        return redirect('index')

    paginator = Paginator(bike_list, 12)
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