from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns for your project
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('', views.home, name='home'),
    path('district/<int:district_id>/', views.district_wikipedia, name='district_wikipedia'),
    path('logout', views.logout, name='logout'),
    path('applicant/', views.applicant_form_view, name='applicant_form'),
    path('success/', views.success, name='success'),
    path('api/get_branches/', views.get_branches_api, name='get_branches_api'),
    # path('get_branches/<int:district_id>/', views.get_branches, name='get_branches'),
]
