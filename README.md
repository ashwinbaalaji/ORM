# Ex02 Django ORM Web Application
# Date:29.09.2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```
models.py:
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

admin.py:
from django.contrib import admin
from .models import Car,CarAdmin
admin.site.register(Car,CarAdmin)

```

# OUTPUT
![alt text](<Screenshot 2025-09-29 102231.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
