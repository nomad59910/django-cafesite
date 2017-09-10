# -*- coding: utf-8 -*-


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart


    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True


    def clear(self):
        self.cart = {}
        self.save()


    def remove(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def add(self, product_id, quantity):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id] = min(quantity + self.cart[product_id], 50)
        else:
            self.cart[product_id] = min(quantity, 50)

        self.save()


    def set(self, product_id, quantity):
        self.cart[str(product_id)] = min(quantity, 50)
        self.save()


    def get(self):
        return self.cart
