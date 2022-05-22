from rest_framework import serializers
from .models import Book


class CreateBookListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result = [Book(**attrs) for attrs in validated_data]
        Book.objects.bulk_create(result)
        return result


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price')
        list_serializer_class = CreateBookListSerializer


