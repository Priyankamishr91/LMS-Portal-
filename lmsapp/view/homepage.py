from django.shortcuts import render
from lmsapp.models import Course
from django.shortcuts import HttpResponse
from django.views.generic import ListView

class HomePageView(ListView):
    template_name = "courses/home.html"
    queryset=Course.objects.filter(active=True)
    context_object_name = 'courses'