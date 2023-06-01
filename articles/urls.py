from django.urls import path
from .views import ArticleListView, update

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view() , name ='articles' ),
    path('update/', update, name = 'update')

]