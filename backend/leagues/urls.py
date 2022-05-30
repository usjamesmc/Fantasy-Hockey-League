from django.urls import path
from leagues import views

urlpatterns = [
    path('', views.new_league)
]
