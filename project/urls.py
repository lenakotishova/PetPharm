from django.urls import path
from . import views

app_name = 'petpharm'
urlpatterns = [
    path('', views.all_medicines, name='all_medicines'),
]
