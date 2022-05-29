from django.urls import path
from goalies import views

urlpatterns = [
    path('<id>/', views.team_goalies),
]
