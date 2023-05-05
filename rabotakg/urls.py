from django.urls import path
from .views import VacancyList, JobDetail

urlpatterns = [
    path('vacancy/', VacancyList.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', JobDetail.as_view(), name='vacancy_detail'),
]