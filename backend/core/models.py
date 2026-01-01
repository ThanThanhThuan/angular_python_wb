from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('researcher', 'Researcher'),
        ('policymaker', 'Policymaker'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='student')

class Country(models.Model):
    iso_code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

class IndicatorData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    indicator_code = models.CharField(max_length=50)
    year = models.IntegerField()
    value = models.FloatField()

    class Meta:
        indexes = [models.Index(fields=['country', 'indicator_code', 'year'])]