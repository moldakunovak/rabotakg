from rest_framework import serializers
from .models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'description', 'requirements', 'company_name', 'location',
                  'pub_date', 'view_count', 'contact_info')