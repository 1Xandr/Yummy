from django.shortcuts import render, HttpResponse
from .models import Categories, Dishes, About_Us, Stats, Why_us, Home


# Create your views here.

def base_view(request):
    categories = Categories.objects.filter(is_visible=True)
    dish = Dishes.objects.filter(is_visible=True)
    about = About_Us.objects.all()
    stats = Stats.objects.all()
    why = Why_us.objects.all()
    home = Home.objects.all()

    data = {
        'categories': categories,
        'dish': dish,
        'about': about,
        'stats': stats,
        'why': why,
        'home': home,
    }
    return render(request, 'main.html', context=data)
