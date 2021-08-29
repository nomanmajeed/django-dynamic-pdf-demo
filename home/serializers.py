from rest_framework import fields, serializers

from .models import Book, Category, Student
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()

        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ["name", "age"]
        # exclude = ["id"]

    def validate(self, data):
        """
        Function for Custom Validations of Data before any Query or Processing
        """

        if data["age"] < 18:
            raise serializers.ValidationError({"error": "Age can't be less than 18"})

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = "__all__"
        """
        depth = 1

        It is used when you want all serialized data from related table with foriegn keys.
        If you want some fileds i-e fields = ['category'] in CategorySerializer then you need
        to explicitly call Category Serializer i-e category = CategorySerializer()
        """
