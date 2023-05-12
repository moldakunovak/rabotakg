from django_filters import rest_framework as rest_filters, CharFilter

from .models import Region, Vacancy, Category

class VacancyFilter(rest_filters.FilterSet):
    vacancy_category = CharFilter(field_name='vacancy_category__title', lookup_expr='icontains')
    region = CharFilter(field_name='region__title', lookup_expr='icontains')

    class Meta:
        model = Vacancy
        fields = ['vacancy','region','vacancy_category']


class CategoryFilter(rest_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Category
        fields = ['title']


class RegionFilter(rest_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Region
        fields = ['title']