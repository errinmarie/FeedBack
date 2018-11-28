from django.shortcuts import render

# Bring in the DogAppointment model and the Sitter model from the models file
from .models import (
    DogAppointment,
    Sitter,
)

def homepage(request):
    # Show all dogs on the homepage
    dogs = DogAppointment.objects.all()
    sitters = Sitter.objects.all()
    context = {
        'dogs': dogs,
        'sitters': sitters,
    }
    return render(request, 'homepage.html', context)


def add_dog(request):
    context = {}

    # First, check if they have submitted something:
    if 'dogname' in request.POST:

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


def add_sitter(request):
    context = {}

    # First, check if the method is POST, that is, they have done a POST form
    # submit (slightly better method than above since it's more generalized)
    if request.method == 'POST':

        # Then, get the data out of the POST dictionary
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        # Finally, actually create the Sitter
        Sitter.objects.create(
            first_name=first_name,
            last_name=last_name,
        )

    return render(request, 'add_sitter.html', context)
    
    
    
    
    
    
    
    
    
    
    
    
