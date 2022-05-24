from datetime import datetime
from rest_framework import serializers
from main.models import BookJournalBase, Book, Journal
from django.contrib.auth.models import User


class BookJournalBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'num_pages', 'genre', 'name', 'price', 'description', 'created_at')


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'type', 'publisher', 'name', 'price', 'description', 'created_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'is_active', 'is_superuser')