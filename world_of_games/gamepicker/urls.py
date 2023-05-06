from django.urls import path
from . import views

urlpatterns = [
    path('game_picker/', views.game_picker)
]
