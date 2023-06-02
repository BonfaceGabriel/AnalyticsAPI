from django.db import models

class Company(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    employees = models.IntegerField()
    headquarters = models.CharField(max_length=255)
    industry_code = models.CharField(max_length=10)
    year_founded = models.IntegerField()

    