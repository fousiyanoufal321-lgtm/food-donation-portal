from django.shortcuts import render, redirect
from .models import FoodDonation

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "Fousiya K" and password == "90807060":
            return redirect("available_food_list")
    return render(request, "donations/login.html")

def donate_view(request):
    donations = FoodDonation.objects.all().order_by("-id")
    return render(request, "donations/donate.html", {"donations": donations})

def dashboard_view(request):
    donations = FoodDonation.objects.all().order_by("-id")
    return render(request, "donations/dashboard.html", {"donations": donations})

def available_food_list(request):
    donations = FoodDonation.objects.all()
    return render(request, "donations/donation_list.html", {"donations": donations})

def create_food_donation(request):
    if request.method == "POST":
        food_name = request.POST.get("food_item")
        quantity = request.POST.get("quantity")
        location = request.POST.get("location")
        if food_name and quantity and location:
            FoodDonation.objects.create(food_name=food_name, quantity=quantity, location=location)
            return redirect("dashboard")
    return render(request, "donations/create_food_donation.html")

def create(request):
    return create_food_donation(request)

