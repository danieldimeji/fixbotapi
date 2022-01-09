from django.urls import path
from . import views

urlpatterns = [
    path('data', views.TelemetricDataListAPIView.as_view()),
    path('data/<int:id>', views.TelemetricDataDetailsAPIView.as_view()),
    
    path('', views.FrontendView.as_view(), name='frontend-view'),
]