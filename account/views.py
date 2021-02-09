from django.shortcuts import render
from django.views.generic import ListView
from book.models import Book


class BookList(ListView):
    template_name = 'registrations/list_book.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Book.objects.all()
        else:
            return Book.objects.filter(status='p')