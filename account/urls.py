from django.urls import path
from .views import BookList,BookCreate

app_name='account'
urlpatterns = [
    path('list',BookList.as_view(),name='list_book'),
    path('create',BookCreate.as_view(),name='create_book'),
]