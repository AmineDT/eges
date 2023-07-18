from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Landing page (index)
    path('activities/', views.activity_list, name='activity_list'),
    path('partners/', views.partner_list, name='partner_list'),
]
