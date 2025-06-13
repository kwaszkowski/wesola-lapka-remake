from django.shortcuts import render
from .models import Course  # import the model

def home(request):
    courses = Course.objects.all().order_by("date")
    return render(request, "core/home.html", {"courses": courses})

def course_table(request):
    courses = Course.objects.all().order_by("date")
    return render(request, "core/courses.html", {"courses": courses})