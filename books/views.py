from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class BookListView(ListView):
    model = Book
    template_name = 'home.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    fields = '__all__'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_edit.html'
    fields = '__all__'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home')
# Create your views here.
