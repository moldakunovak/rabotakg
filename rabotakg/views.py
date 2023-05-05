from requests import Response
from rest_framework import generics
from django.db.models import Q
from .models import Vacancy
from .serializers import VacancySerializer


class VacancyList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.query_params.get('keyword')
        location = self.request.query_params.get('location')
        if keyword and location:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword),
                                        location__icontains=location).order_by('-pub_date')
        return queryset


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
