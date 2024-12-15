
from django.urls import path
from . import views
from .views import send_email

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact"),
    path('movies/', views.movies, name="movies"),
    path('games/', views.games, name="games"),
    path('accessories/', views.accessories_list, name='accessories_list'),
    path('order-accessory/', views.order_accessory, name='order_accessory'),
    path('VR/', views.VR, name="VR"),
    path('send-email/', send_email, name='send_email'),
    path('order-game/', views.order_game, name='order_game'),  # New order URL
    path('order-movie/', views.order_movie, name='order_movie'),  # New order URL
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
