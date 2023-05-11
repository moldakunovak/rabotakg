# coding=utf-8
from django.urls import path, include
# from rest_framework import routers
# from .views import VacancyViewSet

# router = routers.DefaultRouter()
# router.register(r'vacancy', VacancyViewSet,  basename='vacancy')
# router.register(r'vacancy_detail', VacancyDetail,  basename='vacancy-detail')


# urlpatterns = [
#     path('', include(router.urls)),
# ]


# from django.urls import path
# from rest_framework import routers
#
from . import views
from .views import VacancyList, VacancyDetail, VacancyUpdate
#
urlpatterns = [
    path('vacancy/', VacancyList.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancy/<int:pk>/update/', VacancyUpdate.as_view())
]

# rabota_router = routers.DefaultRouter()
# rabota_router.register(r'vacancy', views.VacancyList.as_view())
# rabota_router.register(r'vacancy', views.VacancyDetail.as_view())
# router = routers.DefaultRouter()