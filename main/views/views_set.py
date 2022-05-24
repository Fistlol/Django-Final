from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Book, Journal
from ..serializers import UserSerializer, BookSerializer, JournalSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer = BookSerializer
    
    def allow(self):
        if self.action=='list':
            permission_classes=(isAuthenticated,)
        else:
            permission_classes=(isAdminUser,)
        return [permission() for permission in permission_classes]


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer = JournalSerializer
    
    def allow(self):
        if self.action=='list':
            permission_classes=(isAuthenticated,)
        else:
            permission_classes=(isAdminUser,)
        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)