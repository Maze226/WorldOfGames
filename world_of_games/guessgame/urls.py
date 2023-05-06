from django.urls import path
from . import views

urlpatterns = [
    path('guess_game/', views.guess_game)
]
