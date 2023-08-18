from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
from datetime import date


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class USER(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    class meta:
        verbose_name = 'USER'
        verbose_name_plural = 'USERS'


class Author(models.Model):
    name = models.CharField(max_length=70, unique=True)
    title = models.CharField(max_length=70, )
    personal_info = models.TextField()
    genre = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    birth_country = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField()

    def __str__(self):
        return self.name + self.title

    class meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    name = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Quote(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book', blank=True, null=True)
    upload_time = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, related_name='quotes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quotes')
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'


class interact(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='interactions')
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='interactions')
    like = models.BooleanField()

    def __str__(self):
        return self.user.username + self.quote.content

    class Meta:
        verbose_name = 'Interaction'
        verbose_name_plural = 'Interactions'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
