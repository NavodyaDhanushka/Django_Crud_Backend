from django.urls import path
from students.views import create_student

urlpatterns = [
    path("students/", create_student),
]