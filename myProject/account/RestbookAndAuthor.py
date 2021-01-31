from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=200)
  added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=300)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=timezone.now)


#serializers

from rest_framework import serializers
#from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'added_by', 'created_by']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'created_date', 'author', 'added_by']




#views
#from .serializers import BookSerializer
#from .models import Book
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_books(request):
    user = request.user.id
    books = Book.objects.filter(added_by=user)
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)


import json
from django.core.exceptions import ObjectDoesNotExist

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_book(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        author = Author.objects.get(id=payload["author"])
        book = Book.objects.create(
            title=payload["title"],
            description=payload["description"],
            added_by=user,
            author=author
        )
        serializer = BookSerializer(book)
        return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_book(request, book_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        book_item = Book.objects.filter(added_by=user, id=book_id)
        # returns 1 or 0
        book_item.update(**payload)
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_book(request, book_id):
    user = request.user.id
    try:
        book = Book.objects.get(added_by=user, id=book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from django.urls import include, path
from . import views

urlpatterns = [

  path('getbooks', views.get_books),
  path('addbook', views.add_book),
  path('updatebook/<int:book_id>', views.update_book),
  path('deletebook/<int:book_id>', views.delete_book)
]

"""
> Request
$ curl -X PUT -H "Authorization: Token 9992e37dcee4368da3f720b510d1bc9ed0f64fca" -d '{"title":"CRUD Django Updated V2", "description":"Walkthrough for CRUD in DJANGO", "author": 1}' localhost:8000/api/updatebook/1

> Response
{"book": {
    "id": 1, 
    "title": "CRUD Django Updated V2", 
    "description": "Walkthrough for CRUD in DJANGO", 
    "author": 1, 
    "added_by": 2, 
    "created_date": "2020-02-29T21:07:27.968463Z"
  }
}  

"""
