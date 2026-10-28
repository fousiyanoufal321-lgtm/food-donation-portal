from django.db import models

class FoodDonation(models.Model):
    food_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    ngo_name = models.CharField(max_length=100, blank=True, null=True)  # ????? ?????
    status = models.CharField(max_length=20, default="Available")
    expiry_date = models.DateField(null=True, blank=True)
    expiry_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.food_name

