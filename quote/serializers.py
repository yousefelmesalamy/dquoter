from rest_framework import serializers
from .models import *
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ('id', 'username', 'email', 'password',)
        read_only_fields = ('id', 'date_joined',)
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'username': {'required': True}
        }

    def create(self, validated_data):
        user = USER.objects.create_user(**validated_data)
        return user

    # لو بوست شغل الفاليديشن
    # ال هي بتاع اليوزر اللي بيعمل ابديت اعملع اكسبشن
    # vlaidations
    # validate password
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return value

    # validate email
    def validate_email(self, value):
        if USER.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    # validate username
    def validate_username(self, value):
        if USER.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class InteractSerializer(serializers.ModelSerializer):
    class Meta:
        model = interact
        fields = '__all__'
