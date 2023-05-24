from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentView.as_view(), name='appointment'),
    path('service-finally/', views.ServiceFinallyView.as_view(), name='serviceFinally'),
]