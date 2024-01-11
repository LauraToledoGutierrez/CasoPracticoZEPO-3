from django.urls import path
from .views import test_password

urlpatterns = [
    path('test_password/<str:password>/', test_password),
]
