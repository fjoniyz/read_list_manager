from django.urls import path
from .views import BookDeleteView, BookCreateView, BookDetailView, BookListView, BookUpdateView

urlpatterns = [
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('book/new/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit', BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('', BookListView.as_view(), name='home')
]