from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from main.models import BookJournalBase, Book, Journal
from main.serializers import BookJournalBaseSerializer, BookSerializer, JournalSerializer


class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class JournalAPIView(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [IsAuthenticated]