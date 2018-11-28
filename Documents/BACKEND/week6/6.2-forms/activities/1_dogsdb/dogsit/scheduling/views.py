from django.shortcuts import render

# Bring in the Dog model from the models file
from .models import DogAppointment

def homepage(request):
    # Show all dogs on the homepage
    dogs = DogAppointment.objects.all()
    context = {
        'dogs': dogs,
    }
    return render(request, 'homepage.html', context)

def add_dog(request):
    context = {}
    DogAppointment.objects.create(
        image_src="http://cdn.shibe.online/shibes/1fc9a53355b767a146fa7e6188c88ee557e77659.jpg",
        name="Good Boye",
        age=5,
        date="Tomorrow",
        time="Early in the morning",
    )
    return render(request, 'add_dog.html', context)
    
def add_another_dog(request):
    context = {}
    DogAppointment.objects.create(
        image_src="http://cdn.shibe.online/shibes/1fc9a53355b767a146fa7e6188c88ee557e77659.jpg",
        name="Bad Boye",
        age=5,
        date="Tomorrow",
        time="Early in the morning",
    )
    return render(request, 'add_dog.html', context)
    
def custom_dog(request):
    context = {}
    DogAppointment.objects.create(
        image_src="http://cdn.shibe.online/shibes/1fc9a53355b767a146fa7e6188c88ee557e77659.jpg",
        name="",
        age=,
        date="",
        time="",
    )
    return render(request, 'add_dog.html', context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
