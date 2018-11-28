from django.shortcuts import render, redirect
from django import forms

# Bring in the DogAppointment model and the Sitter model from the models file
from .models import (
    DogAppointment,
    Sitter,
)

class SitterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    
class AppointmentForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    owner = forms.CharField(label='Owner', required=True)
    age = forms.CharField(label='Age', required=True)

form = AppointmentForm()
context = {
'form': form,
    }

def homepage(request):
    sitters = Sitter.objects.all()
    dogs = DogAppointment.objects.all()
    context = {
        'sitters': sitters,
        'dogs': dogs,
    }
    return render(request, 'homepage.html', context)


def add_sitter(request):
    # Check if we are getting a post request, that means we are receiving a
    # form submission
    if request.method == 'POST':
        # Let's get all the values out of the POST dictionary
        form = SitterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            # TODO: Finish this...

            # Finally, actually create the Sitter
            Sitter.objects.create(
                first_name=first_name,
                last_name=last_name,
            )

            # Redirect to homepage to see result
            return redirect('/')
    else:
        form = SitterForm()

    context = {
        'form': form,
    }


    return render(request, 'add_sitter.html', context)


def add_dog(request):
    # Let's start with "no error", but then if something wasn't filled out
    # right, we'll have to add it in here
    context = {
        'error': None,
    }

    # Check if we are getting a post request, that means we are receiving a
    # form submission
    if request.method == 'POST':

        # Then, get the data out of the POST dictionary
        name = request.POST['dogname']
        age = request.POST['age']
        time = request.POST['time']
        date = request.POST['date']

        # Finally, actually create the appointment
        DogAppointment.objects.create(
            name=name,
            age=age,
            date=date,
            time=time,
        )

    return render(request, 'add_dog.html', context)

