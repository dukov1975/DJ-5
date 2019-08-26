from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import Book
from datetime import datetime


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    

class BookDateView(ListView):
    model = Book
    template_name = 'books/book_date.html'
    context_object_name = 'books'

    def get_queryset(self):
        self.name = get_object_or_404(Book, pub_date=self.kwargs['pub_date'])
        return Book.objects.filter(name=self.name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        published_date = context['books'][0].pub_date
        
        try:
            next_date = Book.objects.filter(
                    pub_date__gt=published_date
                ).order_by(
                    'pub_date'
                ).first().pub_date
        except AttributeError:
            next_date = published_date
        
        try:
            prev_date = Book.objects.filter(
                    pub_date__lt=published_date
                ).order_by(
                    '-pub_date'
                ).first().pub_date
        except AttributeError:
            prev_date = published_date

        context['next'] = datetime.strftime(next_date, "%Y-%m-%d")
        context['previous'] = datetime.strftime(prev_date, "%Y-%m-%d")

        return context
