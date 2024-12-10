from django.urls import path
from .views import EmployeeListAPIView

urlpatterns = [
    path('api/employees/', EmployeeListAPIView.as_view(), name='employee_list'),
]
