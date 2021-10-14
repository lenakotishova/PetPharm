from django.urls import path
from . import views

app_name = 'petpharm'
urlpatterns = [
    path('', views.all_medicines, name='all_medicines'),
    path('<int:y>/<int:m>/<int:d>/<slug:slug>', views.detailed_medicine,
         name='detailed_medicine'),
]
