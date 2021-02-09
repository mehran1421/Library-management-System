from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from book.models import Book
from account.models import User


class BookList(ListView):
    template_name = 'registrations/list_book.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Book.objects.all()
        else:
            return Book.objects.filter(status='p')

class MemberList(ListView):
    template_name = 'registrations/list_member.html'
    queryset = User.objects.all()


class BookCreate(CreateView):
    model = Book
    fields = ['title','slug','category','description','author','thumbnail','status']
    template_name = 'registrations/add_book.html'
    success_url = reverse_lazy("account:list_book")