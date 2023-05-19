from rest_framework import serializers
from .models import Category, Product, UserData


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'category', 'description', 'image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "name", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["email", "name"]
