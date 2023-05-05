
from django.urls import path

from . import views
from .views import UserCreate, UserList, UserDetail

urlpatterns = [
    path('user', UserList.as_view()),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('<int:pk>/', UserDetail.as_view()),
    path('register/', UserCreate.as_view()),
]
