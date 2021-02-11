from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,DeleteView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from book.models import Book, Issue
from .mixins import SuperUserAccessMixin, FormValidMixin,FormDeleteMixin,FormRenewMixin
from account.models import User
from django.db.models import Q


class BookList(LoginRequiredMixin, ListView):
    template_name = 'registrations/list_book.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Book.objects.all()
        else:
            return Book.objects.filter(status='p')


class MemberList(SuperUserAccessMixin, ListView):
    template_name = 'registrations/list_member.html'
    queryset = User.objects.all()


class BookCreate(SuperUserAccessMixin, CreateView):
    model = Book
    fields = ['title', 'slug', 'category', 'description', 'author', 'thumbnail', 'status']
    template_name = 'registrations/add_book.html'
    success_url = reverse_lazy("account:list_book")


class IssueBook(SuperUserAccessMixin, FormValidMixin, CreateView):
    model = Issue
    fields = ['slugBook', 'slugUser']
    template_name = 'registrations/issue_book.html'
    success_url = reverse_lazy("account:list_book")


class IssueList(LoginRequiredMixin,ListView):
    template_name = 'registrations/issue_list.html'
    queryset = Issue.objects.all()
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Issue.objects.all()
        else:
            return Issue.objects.filter(slugUser=self.request.user.slug)


class IssueUpdate(SuperUserAccessMixin,FormRenewMixin,UpdateView):
    model = Issue
    template_name ='registrations/issue_book.html'
    fields = ['slugBook', 'slugUser']


class Submitions(SuperUserAccessMixin,FormDeleteMixin,DeleteView):
    model = Issue
    template_name = 'registrations/issue_confirm_delete.html'
    success_url = reverse_lazy('account:issue_list')


class SearchIssueList(SuperUserAccessMixin,ListView):
    paginate_by=6
    template_name="registrations/issue_list.html"

    def get_queryset(self):
        global search
        search=self.request.GET.get('q')
        return Issue.objects.filter(Q(slugBook__icontains=search)|Q(slugUser__icontains=search))


class SearchBookList(ListView):
    paginate_by=6
    template_name="registrations/list_book.html"

    def get_queryset(self):
        global search
        search=self.request.GET.get('q')
        return Book.objects.filter(Q(slug__icontains=search)|
                                   Q(title__icontains=search)|
                                   Q(author__icontains=search)|
                                   Q(description__icontains=search)|
                                   Q(category__title__icontains=search),status='p')


