from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_number=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    man_date=models.DateField()
    email=models.EmailField()
    Type=models.CharField(max_length=10)
class CarAdmin(admin.ModelAdmin):
    list_display=["car_number","name","man_date","email","Type"]

