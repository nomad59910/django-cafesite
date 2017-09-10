from rest_framework import serializers
from product.models import Dish


class CartDishSerializer(serializers.ModelSerializer):

    quantity = serializers.SerializerMethodField()

    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'quantity', 'image')

    def get_quantity(self, obj):
        cart = self.context['cart']

        if cart.get()[str(obj.id)]:
            return cart.get()[str(obj.id)]

        return 0
