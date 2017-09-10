from django.conf import settings
from django.utils.translation import activate
import re


class ForceInRussia(object):

    def process_request(self, request):
        if re.match(".*admin/", request.path):
            activate("ru")