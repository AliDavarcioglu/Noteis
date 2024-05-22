from . import views
from django.urls import path


urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login_page_view, name='login'),
    path('register/', views.register_page_view, name='register'),
]
