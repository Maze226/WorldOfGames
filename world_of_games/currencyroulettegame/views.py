from django.shortcuts import render


# Create your views here.
def currency_roulette(request):
    return render(request, 'currency_roulette.html')
