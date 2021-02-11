from django.http import Http404
from django.shortcuts import redirect,get_object_or_404
from book.models import Book,Issue
from django.utils import timezone


class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404


class FormValidMixin():
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        try:
            mybook = Book.objects.get(slug=self.obj.slugBook, status='p')
        except:
            return redirect('account:issue')

        self.obj.renewCount = 0
        mybook.status = 'd'
        mybook.save()
        return super().form_valid(form)


class FormDeleteMixin():
    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issueBook=get_object_or_404(Issue,pk=pk)
        try:
            mybook = Book.objects.get(slug=issueBook.slugBook)
        except:
            raise Http404

        mybook.status = 'p'
        mybook.save()
        return super().dispatch(request, *args, **kwargs)


class FormRenewMixin():
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.renewCount +=1
        self.obj.created=timezone.now()
        return super().form_valid(form)