from django.urls import path
from .views import BookList, BookCreate, MemberList, IssueBook, IssueUpdate, IssueList,Submitions,SearchIssueList

app_name = 'account'
urlpatterns = [
    path('book/list', BookList.as_view(), name='list_book'),
    path('book/create', BookCreate.as_view(), name='create_book'),
    path('user/list', MemberList.as_view(), name='list_member'),
    path('issue', IssueBook.as_view(), name='issue'),
    path('issue/list', IssueList.as_view(), name='issue_list'),
    path('issue/update/<int:pk>', IssueUpdate.as_view(), name='issue_update'),
    path('issue/delete/<int:pk>', Submitions.as_view(), name="issue-delete"),
    path('issue/search', SearchIssueList.as_view(), name="issue-search"),
]
