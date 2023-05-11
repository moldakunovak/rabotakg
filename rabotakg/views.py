# coding=utf-8
from requests import Response
from rest_framework import generics
from rest_framework.response import Response
from .models import Vacancy
from .serializers import VacancySerializer


class VacancyList(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def get_queryset(self):
        queryset = Vacancy.objects.all()
        keyword = self.request.query_params.get('keyword')
        location = self.request.query_params.get('location')
        if keyword and location:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword),
                                        location__icontains=location).order_by('-pub_date')
        elif keyword:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword)).order_by('-pub_date')
        elif location:
            queryset = queryset.filter(location__icontains=location).order_by('-pub_date')
        return queryset




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
