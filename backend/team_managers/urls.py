from django.urls import path
from team_managers import views

urlpatterns = [
    path('', views.new_manager)
]
