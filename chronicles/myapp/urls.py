from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogpost/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('blogpost/<int:pk>/like/', views.like_post, name='like_post'),
]


# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)