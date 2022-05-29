from django.urls import path
from skaters import views

urlpatterns = [
    path('<id>/', views.team_skaters),
]
