from django.urls import path
from goalies import views

urlpatterns = [
    path('', views.any_goalies),
    path('<id>/', views.chosen_goalies)
]
