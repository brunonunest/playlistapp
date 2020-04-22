from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='home'),
    path('register/', views.RegisterView, name='register_url'),
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('accounts/dashboard/', views.DashboardView, name='accounts/dashboard'),
    path('logout/dashboard/', views.IndexView, name='accounts/dashboard'),
    path('accounts/login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='dashboard/'), name='logout'),
]