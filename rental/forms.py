from django import forms

from .models import *


class AddRentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        exclude =['bicycle']
        widgets = {
            'start_date' : forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        print('somebody called the cleaner!')
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        finish = cleaned_data.get('return_date')

        if not finish:
            print('providing date for <null> return value')
            finish = date.today()

        if (date.today() - start).days > 3650:
            msg = "You're too old for us! Get outta here, Gramps!"
            self.add_error('start_date', msg)

        if finish <= start:
            msg = 'Return date must be later than rental start date'
            self.add_error('return_date', msg)

        if (finish - start).days > 30:
            msg = 'Maximum rental is 30 days'
            self.add_error('return_date', msg)

        if start > date.today():
            msg = 'Sorry, at this time we cannot reserve rentals for the future'
            self.add_error('start_date', msg)


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'