# coding=utf-8
from django.urls import path, include
from .views import VacancyList, VacancyDetail, VacancyUpdate, CategoryDetail, TopVacancyList, RegionList, CategoryList, \
    TopVacancyDetail, RegionDetail

urlpatterns = [
    path('vacancy/', VacancyList.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancy/<int:pk>/update/', VacancyUpdate.as_view()),
    # path('company/', CompanyList.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='vacancy_detail'),
    path('top/', TopVacancyList.as_view()),
    path('top/<int:pk>/', TopVacancyDetail.as_view()),
    path('region/', RegionList.as_view()),
    path('region/<int:pk>/', RegionDetail.as_view()),
]

