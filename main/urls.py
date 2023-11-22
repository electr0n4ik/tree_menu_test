from django.urls import path

from .views import index

app_name = 'main'

urlpatterns = [
    path('home/', index, {'name': 'Home'}, name='home'),
    path('company/', index, {'name': 'About company'}, name='company'),
    path('development/', index, {'name': 'Development'}, name='development'),
    path('development/cpp', index, {'name': 'Development C++'},
         name='development_cpp'),
    path('development/cpp/qt', index, {'name': 'Development C++/Qt'},
         name='development_cpp_qt'),
    path('development/python', index, {'name': 'Development Python'},
         name='development_python'),
    path('development/python/django', index,
         {'name': 'Development Python/Django'},
         name='development_python_django'),
    path('development/python/tornado', index,
         {'name': 'Development Python/Tornado'},
         name='development_python_tornado'),
    path('prices/', index, {'name': 'Prices'}, name='prices'),
]
