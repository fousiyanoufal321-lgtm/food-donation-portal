from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("donate/", views.donate_view, name="donate"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("available/", views.available_food_list, name="available_food_list"),
    path("create/", views.create_food_donation, name="create_food_donation"),
]

