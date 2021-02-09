from django.urls import path
from .views import BookList,BookCreate,MemberList

app_name='account'
urlpatterns = [
    path('listbook',BookList.as_view(),name='list_book'),
    path('create',BookCreate.as_view(),name='create_book'),
    path('listuser',MemberList.as_view(),name='list_member'),
]