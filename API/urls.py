from django.urls import path, include
from .views import UserList,  UserDetail,  CryptoList, CryptoDetail, api_manual


app_name = 'API'


urlpatterns = [
    path('', api_manual, name='main'),
    path('crypto/', CryptoList.as_view(), name='crypto_list'),
    path('crypto/<slug:slug>/', CryptoDetail.as_view(), name='crypto_detail'),
    path('user/', UserList.as_view(), name='user_list'),
    path('user/<int:pk>', UserDetail.as_view(), name='user'),
]
