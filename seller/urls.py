from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all, name='get_all'),
    path('add', views.post_seller, name='post_seller'),
]
