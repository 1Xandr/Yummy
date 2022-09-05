from django.shortcuts import render, HttpResponse, redirect
from .models import Categories, Dishes, About_Us, Stats, Why_us, Home, Testimonials, Event, Chefs, Gallery
from .forms import UserReservationForm

# Create your views here.


def base_view(request):

    if request.method == 'POST':
        reservation = UserReservationForm(request.POST, prefix='reservation')
        if reservation.is_valid():
            reservation.save()
            return redirect('/')

    categories = Categories.objects.filter(is_visible=True)
    dish = Dishes.objects.filter(is_visible=True)
    about = About_Us.objects.all()
    stats = Stats.objects.all()
    why = Why_us.objects.all()
    home = Home.objects.all()
    testimonials = Testimonials.objects.filter(is_visible=True)
    event = Event.objects.filter(is_visible=True)
    chefs = Chefs.objects.all()
    gallery = Gallery.objects.all()
    reservation = UserReservationForm()

    for item in categories:
        item.dish = Dishes.objects.filter(is_visible=True).filter(categories=item.pk)

    data = {
        'categories': categories,
        'dish': dish,
        'about': about,
        'stats': stats,
        'why': why,
        'home': home,
        'testimonials': testimonials,
        'event': event,
        'chefs': chefs,
        'gallery': gallery,
        'reservation': reservation,
    }
    return render(request, 'main.html', context=data)
