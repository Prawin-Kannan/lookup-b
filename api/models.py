from django.db import models

class HomeLead(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    raw_json = models.JSONField()
    urn = models.CharField(max_length=50)
    lead_id = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class HomeEmployee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    seniority = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    ranking = models.IntegerField()
    selected_status = models.BooleanField(default=False)
    raw_json = models.JSONField()
