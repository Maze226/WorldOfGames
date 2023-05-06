from django.urls import path
from . import views

urlpatterns = [
    path('save_game/', views.save_game)
]
