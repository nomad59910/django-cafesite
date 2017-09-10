from rest_framework import serializers
from product.models import Dish, Ingredients, TypeDish, TypeIngredients


class DishPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'image', 'price', )


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id', 'name')


class TypeDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDish
        fields = ('id', 'name',)


class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True, read_only=True)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'image', 'price', 'description', 'ingredients',)


class TypeDisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDish
        filter = ('id', 'name', 'image',)


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id', 'name')


class AlbumSerializer(serializers.ModelSerializer):
    ingredients = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = TypeIngredients
        fields = ('id', 'name', 'ingredients')
