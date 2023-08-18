from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from .permissons import UserPermission
from rest_framework import filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
            })
        else:
            return Response({"Response": "username or password was incorrect"}, status=status.HTTP_401_UNAUTHORIZED)

def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author_list.html', context)
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 1000
#
#
# # work as viewsets
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = USER.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [UserPermission]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     pagination_class = StandardResultsSetPagination
#     search_fields = ['username', 'email']
#     filterset_fields = ['id', 'username', 'email']
#     lookup_field = 'id'
#     ordering_fields = ['username', 'email']
#
#     def update(self, request, *args, **kwargs):
#         kewargs = {'partial': True}
#         return super().update(request, *args, **kewargs)
#
#
# # caching
# # A certain woman had a very sharp consciousness
# # but almost no memory ... She remembered enough to work, and she worked hard. - Lydia Davis
#
# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = [UserPermission]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     pagination_class = StandardResultsSetPagination
#     search_fields = ['name', 'title', 'genre']
#     filterset_fields = ['id', 'name', 'title', 'genre']
#     lookup_field = 'id'
#     ordering_fields = ['name', 'title']
#
#     def update(self, request, *args, **kwargs):
#         kewargs = {'partial': True}
#         return super().update(request, *args, **kewargs)
#
#
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [UserPermission]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     pagination_class = StandardResultsSetPagination
#     search_fields = ['name', ]
#     filterset_fields = ['id', 'name']
#     lookup_field = 'id'
#     ordering_fields = ['name']
#
#     def update(self, request, *args, **kwargs):
#         kewargs = {'partial': True}
#         return super().update(request, *args, **kewargs)
#
#
# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = [UserPermission]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     pagination_class = StandardResultsSetPagination
#     search_fields = ['name', ]
#     filterset_fields = ['id', 'name']
#     lookup_field = 'id'
#     ordering_fields = ['name']
#
#     def update(self, request, *args, **kwargs):
#         kewargs = {'partial': True}
#         return super().update(request, *args, **kewargs)
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [UserPermission]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     pagination_class = StandardResultsSetPagination
#     search_fields = ['name', ]
#     filterset_fields = ['id', 'name']
#     lookup_field = 'id'
#     ordering_fields = ['name']
#
#     def update(self, request, *args, **kwargs):
#         kewargs = {'partial': True}
#         return super().update(request, *args, **kewargs)
#
#
# class QuoteViewSet(viewsets.ModelViewSet):
#     queryset = Quote.objects.all()
#     serializer_class = QuoteSerializer
#     permission_classes = [UserPermission]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     pagination_class = StandardResultsSetPagination
#     search_fields = ['quote', 'content', 'author__name', 'author__title', 'author__genre', 'book__name', 'tag__name',
#                      'category__name', ]
#     filterset_fields = ['id',]
#     lookup_field = 'id'
#     ordering_fields = ['quote', 'content', 'author__name', 'author__title', 'author__genre', 'book__name',
#                        'tag__name', ]
#
#     def update(self, request, *args, **kwargs):
#         kewargs = {'partial': True}
#         return super().update(request, *args, **kewargs)
#
#
# class InteractViewSet(viewsets.ModelViewSet):
#     queryset = interact.objects.all()
#     serializer_class = InteractSerializer
#     permission_classes = [UserPermission]
#
#     def update(self, request, *args, **kwargs):
#         kewargs = {'partial': True}
#         return super().update(request, *args, **kewargs)

