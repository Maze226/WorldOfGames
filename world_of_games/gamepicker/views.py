from django.shortcuts import render


# Create your views here.
def game_picker(request):
    return render(request, 'game_picker.html')
