from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('login/', views.login_views, name='login'),
    path('signup/', views.signup_views, name='signup'),
    path('home/',views.homepage, name='homepage'),
    path('FATS_Update/', views.fats, name="fats"),
    path('FATS_Details/', views.fatdetail, name='fatdetail'),
    path('CULT_Update/',views.cult, name="cult"),
    path('CULT_Details/', views.cultdetail, name='cultdetail'),
    path('Paracosm_Update/', views.paracosm, name="paracosm"),
    path('Paracosm_Details/', views.paracosmdetail, name='paracosmdetail'),
    path('Photogeeks_Update/', views.photogeeks, name="photogeeks"),
    path('Photogeeks_Details/', views.photogeeksdetail, name='photogeeksdetail'),
    path('Tech_Update/', views.tech, name="tech"),
    path('Tech_Details/', views.techdetail, name='techdetail'),
    path('Vedant_Samiti_Update/', views.vedant, name="vedant"),
    path('Vedant_Details/', views.vedantdetail, name='vedantdetail'),
    path('Megaheartz_Update/', views.megaheartz, name="megaheartz"),
    path('Megaheartz_Details/', views.megaheartzdetail, name='megaheartzdetail'),
    path('TARS_Update/', views.tars, name="tars"),
    path('TARS_Details/', views.tarsdetail, name='tarsdetail'),
    path('ECELL_Update/', views.ecell, name="ecell"),
    path('ECELL_Details/', views.ecelldetail, name='ecelldetail'),
    path('Sports_Society_Update/', views.sports, name="sports"),
    path('Sports_Society_Details/', views.sportsdetail, name='sportsdetail'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('logout/', views.logout_view, name="logout"),


]