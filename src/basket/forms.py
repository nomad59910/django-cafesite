from django import forms
from product .models import Dish
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label=_("Имя"), required=True)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label=_("Телефон"),)
    date = forms.DateTimeField(label=_("Дата"))
    time = forms.TimeField(label=_("Время"))
    comment = forms.CharField(max_length=400, widget=forms.Textarea,
                              label=_("Комментарий"), required=True)


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateTimeInput(attrs={'type': 'date'})
        self.fields['time'].widget = forms.widgets.TimeInput(attrs={'type': 'time'})


    def send_email(self, cart):
        name = self.cleaned_data['name']
        phone_number = self.cleaned_data['phone_number']
        date = self.cleaned_data['date']
        time = self.cleaned_data['time']
        comment = self.cleaned_data['comment']

        message_templates = settings.MESSAGE_TEMPLATES
        dish_templates = settings.DISH_TEMPLATES

        cart_data = cart.get()
        dishs_email = ""
        total = 0
        for dish_id in cart_data.keys():
            dish = Dish.objects.get(id=dish_id)
            dishs_email += dish_templates.format(name=dish.name, price=dish.price,
                count=cart_data[dish_id], total=cart_data[dish_id] * dish.price)
            total += cart_data[dish_id] * dish.price

        message = message_templates.format(name=name, number=phone_number,
                                           day=date, time=time, comment=comment,
                                           dish=dishs_email[:-1], total=total)

        # send_mail('Заказ сенджу кафе', message, settings.EMAIL_HOST_USER,
        #           ["example@gmail.com"], fail_silently=False)

        cart.clear()
