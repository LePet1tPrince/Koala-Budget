from django.views.generic import ListView

from .models import Trxn

class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "feed/trxn_feed.html"
    model = Trxn
    context_object_name = "trxns"
    queryset = Trxn.objects.all().order_by('-Date')[0:50]