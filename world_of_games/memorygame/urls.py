from django.urls import path
from . import views

urlpatterns = [
    path('memory_game/', views.memory_game)
]
