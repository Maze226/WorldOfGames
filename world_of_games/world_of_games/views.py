from django.shortcuts import render


# Create your views here.
def introduction(request):
    return render(request, 'index.html')
