from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete_city/<int:pk>', views.delete_city, name="delete_city"),
]
