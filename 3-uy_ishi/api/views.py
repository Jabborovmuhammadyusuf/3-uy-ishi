from rest_framework import generics
from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Genre.objects.all()
    def get_serializer_class(self):
        return GenreSerializer

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class BookListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Book.objects.all()
    def get_serializer_class(self):
        return BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
