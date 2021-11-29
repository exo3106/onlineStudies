from django.urls import path, include
from .views import Index
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginView,Dashboard,RegisterView,CourseOverview
urlpatterns = [
    path('', Index, name='index'),
    path('login/', LoginView, name='login'),
    path('register/', RegisterView, name='register'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('course-overview/', CourseOverview.as_view(), name='course-overview'),
    #path('logout/', auth_views.logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
