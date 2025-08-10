from django.db import models
from cars.models import Car  # исправленный импорт

class User(models.Model):  # исправленный родитель
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=40)  # лучше CharField для телефонов

    cars = models.ManyToManyField(Car, related_name="owners")  # исправленное имя поля

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
