from django.conf import settings
from django.db import models
from requests import Response


class Region(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    pub_date = models.DateField()
    view_count = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=50)
    contact_info = models.TextField()

    # def increase_view_count(self):
    #     self.view_count += 1
    #     self.save()

    def __str__(self):
        return self.title

class TopVacancy(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE,
                                    related_name='vacancy')


    def __str__(self):
        return self.vacancy.title

