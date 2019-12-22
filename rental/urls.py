from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('customer/<int:cust_id>', views.view_customer, name='view-single-customer'),
    path('all-bike-types', views.view_bike_types, name='view-bike-types'),
    path('bike-types/<bike_type>', views.view_by_type, name='view-by-type'),
    path('add-rental/<int:bike_id>', views.add_rental, name='add-rental'),
    path('view-bikes', views.view_all_bikes, name='view-all-bikes'),
    path('bike/<int:bike_id>', views.bike_page, name='view-bike'),
    path('new-customer', views.add_customer, name='add-customer'),
    path('rental-history', views.view_all_rentals, name='view-all-rentals'),
]