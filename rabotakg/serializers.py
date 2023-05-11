from rest_framework import serializers
from .models import Vacancy, TopVacancy, Category, Region


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"

    # def update(self, instance, validated_data):


# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = "__all__"

class TopVacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = TopVacancy
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"
