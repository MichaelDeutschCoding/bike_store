from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('customer/<int:cust_id>', views.customer, name='view-single-customer'),
    path('bike-types', views.view_bike_types, name='view-bike-types'),
    path('bike-types/<bike_type>', views.view_by_type, name='view-by-type'),
]