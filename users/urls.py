from django.urls import path
from .views import register, login, log_out

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', log_out, name='logout'),
]
