from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Course
# Create your views here.

def Index(request):

    return render(request,'index.html')  
