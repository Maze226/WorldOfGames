from django.urls import path
from . import views

urlpatterns = [
    path('currency_roulette/', views.currency_roulette)
]
