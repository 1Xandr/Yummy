from django.urls import path
from .views import reservations_list, update_reservation

app_name = 'manager'

urlpatterns = [
    path('reservation/', reservations_list, name='reservations_list'),
    path('reservation/update/<int:pk>/', update_reservation, name='update_reserve')
]