from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('author', AuthorViewSet, basename='author')
router.register('book', BookViewSet, basename='book')
router.register('tag', TagViewSet, basename='tag')
router.register('category', CategoryViewSet, basename='category')
router.register('quote', QuoteViewSet, basename='quote')
router.register('interact', InteractViewSet, basename='interact')

urlpatterns = [
    path('quote/', include(router.urls)),
    #login
    path("login/", CustomAuthToken.as_view()),
]
