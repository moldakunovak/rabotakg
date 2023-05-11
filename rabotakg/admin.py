from django.contrib import admin

from rabotakg.models import Vacancy, TopVacancy, Category, Region

admin.site.register(Vacancy)

admin.site.register(TopVacancy)
admin.site.register(Category)
admin.site.register(Region)
