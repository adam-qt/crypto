from django.urls import path
from .views import data_list_view, favourite_list_view ,update,CryptoDetailView, add_to_favourite_list, remove_from_favourite_list
app_name = 'data'
urlpatterns = [
    path('', data_list_view, name='data'),
    path('list/', favourite_list_view, name='favourite_list'),
    path('update/', update, name='update'),
    path('detail/<int:pk>', CryptoDetailView.as_view(), name = 'crypto_detail'),
    path('detail/add/<int:pk>' , add_to_favourite_list , name = 'add_to_fav'),
    path('detail/remove/<int:pk>' , remove_from_favourite_list , name = 'remove_from_fav'),

]
