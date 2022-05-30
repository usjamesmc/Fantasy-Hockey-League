from django.urls import path
from teams import views

urlpatterns = [
    path('', views.new_team)
]
