from django.contrib import admin
from .models import Customer, Rental, RentalRate, BicycleType, FrameMaterial, Bicycle

admin.site.register(Customer)
admin.site.register(Rental)
admin.site.register(RentalRate)
admin.site.register(BicycleType)
admin.site.register(FrameMaterial)
admin.site.register(Bicycle)