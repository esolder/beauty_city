from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentView.as_view(), name='appointment'),
    path('service-finally/', views.ServiceFinallyView.as_view(), name='serviceFinally'),
    path('submit_appointment/', views.submit_appointment, name='submit_appointment'),
    path('submit_review/', views.SubmitReview.as_view(), name='reviews'),
    path('api/submit_review/', views.SubmitReview.as_view(), name='submit_review'),
    path('get-time/', views.get_time, name='get_time'),
    path('tips/', views.TipsView.as_view(), name='tips'),
    path('service-success/', views.ServiceSuccessView.as_view(), name='serviceSuccess'),
]