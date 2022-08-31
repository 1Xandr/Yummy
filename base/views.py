from django.shortcuts import render, HttpResponse
from .models import Categories, Dishes, About_Us, Stats, Why_us, Home, Testimonials, Event, Chefs


# Create your views here.

def base_view(request):
    categories = Categories.objects.filter(is_visible=True)
    dish = Dishes.objects.filter(is_visible=True)
    about = About_Us.objects.all()
    stats = Stats.objects.all()
    why = Why_us.objects.all()
    home = Home.objects.all()
    testimonials = Testimonials.objects.filter(is_visible=True)
    event = Event.objects.filter(is_visible=True)
    chefs = Chefs.objects.all()

    data = {
        'categories': categories,
        'dish': dish,
        'about': about,
        'stats': stats,
        'why': why,
        'home': home,
        'testimonials': testimonials,
        'event': event,
        'chefs' : chefs,
    }
    return render(request, 'main.html', context=data)
