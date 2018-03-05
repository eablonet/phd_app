from django.urls import path, include
from . import views

urlpatterns = [
    path('substrate/', views.substrate_list, name='substrate_list'),
    path(
        'substrate/<int:pk>/', views.substrate_detail, name='substrate_detail'
    )
]
