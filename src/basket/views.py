from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from .forms import ContactForm
from .cart import Cart


class ShowBasketView(FormView):
    template_name = 'basket/basket.html'
    form_class = ContactForm
    success_url = reverse_lazy('basket:success-order')

    def form_valid(self, form):
        cart = Cart(self.request)
        form.send_email(cart)
        return super(ShowBasketView, self).form_valid(form)


class OrderCompletedView(TemplateView):
    template_name = 'basket/order_completed.html'
