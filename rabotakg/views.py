# coding=utf-8
# from django.utils.encoding import force_text
from django.db.models import Q
from urllib.parse import unquote
from requests import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics, permissions
from rest_framework.response import Response
from .filters import VacancyFilter, CategoryFilter, RegionFilter
from .models import Vacancy, Category, TopVacancy, Region, Category
from .serializers import VacancySerializer, CategorySerializer, TopVacancySerializer, \
    RegionSerializer, CategorySerializer

class VacancyList(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = VacancyFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'vacancy_category__title', 'region__title']

    def get_queryset(self):
        queryset = super().get_queryset()

        keyword = self.request.query_params.get('keyword')
        category_id = self.request.query_params.get('category')
        region_id = self.request.query_params.get('region')

        if keyword:
            keyword = unquote(keyword)  # Декодирование URL-кодирования
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(description__icontains=keyword)
            )

        if category_id:
            category_id = unquote(category_id)
            queryset = queryset.filter(category_id=category_id)

        if region_id:
            region_id = unquote(region_id)
            queryset = queryset.filter(region_id=region_id)

        return queryset.order_by('-pub_date')




class VacancyDetail(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        instance.view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class VacancyUpdate(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer



class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = CategoryFilter

class CategoryDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TopVacancyList(generics.ListCreateAPIView):
    queryset = TopVacancy.objects.all()
    serializer_class = TopVacancySerializer
    permission_classes = [permissions.AllowAny]

class TopVacancyDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = TopVacancy.objects.all()
    serializer_class = TopVacancySerializer

class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = RegionFilter

class RegionDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

