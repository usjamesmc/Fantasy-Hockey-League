from django.urls import path
from skaters import views

urlpatterns = [
    path('<id>/', views.chosen_skaters),
    path('', views.new_skater)
]
