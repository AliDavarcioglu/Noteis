from . import views
from django.urls import path


urlpatterns = [
    path('', views.home),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
]
