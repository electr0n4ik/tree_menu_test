from django.shortcuts import render

# Create your views here.


def index(request, name):
    return render(request, 'menu.html', {'name': name})
