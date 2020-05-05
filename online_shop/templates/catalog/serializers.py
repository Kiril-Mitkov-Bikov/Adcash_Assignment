from rest_framework import serializers
from catalog.models import Category, Product

# Serializers for JSON encoded responses


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
            'slug'
        ]
        read_only_fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'slug',
            'image',
            'description',
            'price',
            'stock',
            'available',
            'created,'
            'updated'
        ]
        read_only_fields = ('category', 'name', 'image', 'description', 'price', 'stock, available')


