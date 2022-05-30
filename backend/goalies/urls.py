from django.urls import path
from goalies import views

urlpatterns = [
    path('', views.new_goalie),
    path('<id>/', views.chosen_goalies)
]
