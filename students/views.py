from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student

@csrf_exempt
def create_student(request):
    if request.method == "GET":
        students = Student.objects.all().values()
        return JsonResponse(list(students), safe=False)

    if request.method == "POST":
        data = json.loads(request.body)

        student = Student.objects.create(
            name=data["name"],
            email=data["email"],
            birthday=data["birthday"]
        )

        return JsonResponse({
            "id": student.id,
            "message": "Student created successfully"
        })

