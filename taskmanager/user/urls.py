from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

#app_name = 'user'

urlpatterns = [
    #path('', views.login, name='login'),
    path('registers', views.registers, name='registers'),
    path('test', views.test, name='test'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),

]