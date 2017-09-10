from rest_framework.views import APIView
from basket.cart import Cart
from rest_framework.response import Response
from product.models import Dish
from .serializers import CartDishSerializer


def get_cart_data(cart):
    data_basket = cart.get()

    result = {}
    result["count"] = len(data_basket)
    products = Dish.objects.filter(id__in=list(data_basket.keys()))
    dish_serializer = CartDishSerializer(products, many=True,
                                         context={"cart": cart})

    total = 0
    for item in dish_serializer.data:
        total += item['price'] * item['quantity']

    result["order_total"] = total
    result["products"] = dish_serializer.data

    return result


class AddProductAPIView(APIView):
    def post(self, request):
        cart = Cart(request)
        product_id = int(request.POST['productId'])
        quantity = int(request.POST['count'])
        cart.add(product_id, quantity)

        return Response(get_cart_data(cart))


class SetProductAPIView(APIView):
    def post(self, request):
        cart = Cart(request)
        product_id = int(request.POST['productId'])
        quantity = int(request.POST['count'])
        cart.set(product_id, quantity)
        return Response(get_cart_data(cart))


class RemoveProductAPIView(APIView):
    def post(self, request):
        cart = Cart(request)
        product_id = int(request.POST['id'])
        cart.remove(product_id)
        return Response(get_cart_data(cart))


class GetDataBasket(APIView):
    def get(self, request):
        cart = Cart(request)

        return Response(get_cart_data(cart))
