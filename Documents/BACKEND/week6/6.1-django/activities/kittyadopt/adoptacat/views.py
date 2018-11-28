from django.shortcuts import render

# Create your views here.

def adoption_homepage(request):
    context = {
        'adoptions_needed': 5,
    }
    return render(request, 'adoption_homepage.html', context)

def new_test_page(request):
    context = {
        'adoptions_needed': 5,
    }
    return render(request, 'new_test_page.html', context)
