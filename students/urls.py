from django.urls import path
from .views import (
    StudentListAPIView,
    StudentDetailAPIView,
    StudentCreateAPIView,
    StudentUpdateAPIView,
    StudentDeleteAPIView,
)

urlpatterns = [
    path("students/", StudentListAPIView.as_view(), name="student-list"),

    path("students/<int:pk>/", StudentDetailAPIView.as_view(), name="student-detail"),

    path("students/create/", StudentCreateAPIView.as_view(), name="student-create"),

    path("students/update/<int:pk>/", StudentUpdateAPIView.as_view(), name="student-update"),

    path("students/delete/<int:pk>/", StudentDeleteAPIView.as_view(), name="student-delete"),
]