from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Trxn

class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "feed/trxn_feed.html"
    model = Trxn
    context_object_name = "trxns"
    queryset = Trxn.objects.all().order_by('-Date')[0:50]


class CreateNewTrxn(CreateView):
    model = Trxn
    template_name = "feed/create.html"
    fields = [
        'Date',
        'Amount',
        'Account',
        'Category',
        'Notes',
    ]