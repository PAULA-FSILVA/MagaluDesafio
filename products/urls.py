from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_product>/', views.detail, name="detail"),
    path('create', views.create_product, name='create_product')
]
