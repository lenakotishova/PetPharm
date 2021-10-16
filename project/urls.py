from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class MyHackedView(auth_views.PasswordResetView):
    success_url = reverse_lazy('project:password_reset_done')


app_name = 'project'

urlpatterns = [
    path('', views.all_medicines, name='all_medicines'),
    path('<int:y>/<int:m>/<int:d>/<slug:slug>/', views.detailed_medicine,
         name='detailed_medicine'),
    path('<int:medicine_id>/share/', views.share_medicine, name='share_medicine'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', MyHackedView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('project:password_reset_complete'),
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
