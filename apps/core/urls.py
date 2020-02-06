from django.urls import path
from core.views import HomeView, ReportView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('report/', ReportView.as_view(), name='report'),
]
