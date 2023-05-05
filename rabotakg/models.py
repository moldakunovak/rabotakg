from django.conf import settings
from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextrField()
    requirements = models.TextField()
    company_name = models.CharField(max_length=200)
    pub_date = models.DateField()
    view_count = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=50)
    contact_info = models.TextField()

    def __str__(self):
        return self.title

