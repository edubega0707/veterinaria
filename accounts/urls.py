from django.urls import  path
from .views import ProfileView
from django.contrib.auth import views as logViews


app_name='accounts'

urlpatterns=[
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', logViews.login, name='login'),
    path('logout/', logViews.logout, name='logout'),

]
