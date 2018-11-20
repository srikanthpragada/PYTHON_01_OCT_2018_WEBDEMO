from .serializers import BookSerializer
from rest_framework.response import Response
from .models import Book
from django.shortcuts import render
from rest_framework.decorators import api_view


# Supports get
@api_view(['GET','POST'])
def list_books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        pass


@api_view(['GET', 'DELETE', 'PUT'])
def get_book(request, bookid):
    try:
        book = Book.objects.get(id=bookid)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':  # Update
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        try:
            book.delete()
            return Response(status=204)
        except:
            return Response(status=500)
