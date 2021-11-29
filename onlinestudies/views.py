from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Course
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def Index(request):

    return render(request,'index.html')  

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    return render(request,'registration/login.html')



# class LoginForm(LoginView):
#     template_name = 'registration/login.html'

def RegisterView(request):

    return render(request,'registration/register.html')

class Dashboard(DetailView):
    model = Course
    template_name='student/index.html'

class CourseOverview(ListView):
    model = Course
    template_name='course_overview.html'


