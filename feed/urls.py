from django.urls import path

from . import views

app_name = "feed"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("new/", views.CreateNewTrxn.as_view(), name="new_trxn"),
]

