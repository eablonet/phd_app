from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.substrat_list, name='substrat_list'),
]
