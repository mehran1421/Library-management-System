from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,DeleteView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from book.models import Book, Issue
from .mixins import SuperUserAccessMixin, FormValidMixin,FormDeleteMixin
from account.models import User


class BookList(LoginRequiredMixin, ListView):
    template_name = 'registrations/list_book.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Book.objects.all()
        else:
            return Issue.objects.filter(slugUser=self.request.user.slug)


class MemberList(SuperUserAccessMixin, LoginRequiredMixin, ListView):
    template_name = 'registrations/list_member.html'
    queryset = User.objects.all()


class BookCreate(SuperUserAccessMixin, LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'slug', 'category', 'description', 'author', 'thumbnail', 'status']
    template_name = 'registrations/add_book.html'
    success_url = reverse_lazy("account:list_book")


class IssueBook(SuperUserAccessMixin, FormValidMixin, LoginRequiredMixin, CreateView):
    model = Issue
    fields = ['slugBook', 'slugUser']
    template_name = 'registrations/issue_book.html'
    success_url = reverse_lazy("account:list_book")


class IssueList(SuperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = 'registrations/issue_list.html'
    queryset = Issue.objects.all()


class IssueUpdate(UpdateView):
    template_name ='registrations/issue-update.html'
    fields =['created','renewCount']


class Submitions(SuperUserAccessMixin,FormDeleteMixin,DeleteView):
    model = Issue
    template_name = 'registrations/issue_confirm_delete.html'
    success_url = reverse_lazy('account:issue_list')