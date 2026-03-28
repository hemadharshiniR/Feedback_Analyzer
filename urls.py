from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin dashboard
    path('', include('feedback.urls')),  # Include app URLs (home, events, feedback, history, dashboard)
    path('login/', auth_views.LoginView.as_view(template_name='feedback/login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Logout redirect
]
