from django.urls import path
from .views import BookList

app_name='account'
urlpatterns = [
    path('list',BookList.as_view(),name='list_book')
]