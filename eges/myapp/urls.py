from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Landing page (index)
    path('activities/', views.activity_list, name='activity_list'),
    path('activity/<int:pk>/', views.activity_detail, name='activity_detail'),
    path('partners/', views.partner_list, name='partner_list'),
]


# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)