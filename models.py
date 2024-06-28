from django.db import models
import json

class HomeLead(models.Model):
    company_name = models.CharField(max_length=255)
    number_of_employees = models.IntegerField()
    raw_json = models.JSONField()

    def __str__(self):
        return self.company_name

class HomeEmployee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    seniority = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    company = models.ForeignKey(HomeLead, on_delete=models.CASCADE)
    raw_json = models.JSONField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
