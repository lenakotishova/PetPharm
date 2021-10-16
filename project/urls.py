from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'petpharm'
urlpatterns = [
    path('', views.all_medicines, name='all_medicines'),
    path('<int:y>/<int:m>/<int:d>/<slug:slug>/', views.detailed_medicine,
         name='detailed_medicine'),
    path('<int:medicine_id>/share/', views.share_medicine, name='share_medicine'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
