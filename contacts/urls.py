from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [    
    path('', views.home_view, name='home'),
    path('save_contact/', views.save_contact, name='save_contact'),
]