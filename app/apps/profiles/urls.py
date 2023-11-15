from django.urls import path
from apps.profiles import views

app_name = 'profiles'

urlpatterns = [
    path('signupp/', views.signupp, name='signupp'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]