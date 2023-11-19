from django.contrib import admin
from .models import USER, Author, Quote, Book, Tag, interact, Category, carousel
from django.utils.safestring import mark_safe


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    list_filter = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    list_display_links = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('username', 'email')
    filter_horizontal = ()
    fieldsets = ()


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'genre', 'birth_date', 'death_date', 'birth_country', 'thumbnail')
    list_filter = ('name', 'title', 'genre', 'birth_date', 'death_date', 'birth_country',)
    list_display_links = ('name', 'title', 'genre', 'birth_date', 'death_date', 'birth_country', 'thumbnail')
    search_fields = ('name', 'title', 'genre', 'birth_date', 'death_date', 'birth_country')
    ordering = ('name', 'title', 'genre', 'birth_date', 'death_date', 'birth_country')
    filter_horizontal = ()
    fieldsets = ()

    def thumbnail(self, instance):
        if instance.image.name != '':
            return mark_safe(
                f'<img src="{instance.image.url}" style="width: 70px; height:70px; object-fit: cover; " />')
        return 'No Image'


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'book', 'category', 'upload_time', 'image')
    list_filter = ('author', 'book', 'category')
    list_display_links = ('author', 'book', 'category')
    search_fields = ('author', 'quote', 'book', 'tag', 'category')
    ordering = ('author', 'book', 'category')
    filter_horizontal = ()
    fieldsets = ()


class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'image')
    list_filter = ('author', 'name', 'image')
    list_display_links = ('author', 'name', 'image')
    search_fields = ('author', 'name')
    ordering = ('author', 'name')
    filter_horizontal = ()
    fieldsets = ()


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
    fieldsets = ()


class interactAdmin(admin.ModelAdmin):
    list_display = ('user', 'quote', 'like')
    list_filter = ('user', 'quote', 'like')
    list_display_links = ('user', 'quote', 'like')
    search_fields = ('user', 'quote', 'like')
    ordering = ('user', 'quote', 'like')
    filter_horizontal = ()
    fieldsets = ()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
    fieldsets = ()


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('carousel_title', 'carousel_text', 'thumbnail')
    list_filter = ('carousel_title', 'carousel_text', 'image')
    list_display_links = ('carousel_title', 'carousel_text', 'thumbnail')
    search_fields = ('carousel_title', 'carousel_text', 'image')
    ordering = ('carousel_title', 'carousel_text', 'image')

    def thumbnail(self, instance):
        if instance.image.name != '':
            return mark_safe(
                f'<img src="{instance.image.url}" style="width: 70px; height:70px; object-fit: cover; " />')
        return 'No Image'


admin.site.register(USER, UserAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(interact, interactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(carousel, CarouselAdmin)
