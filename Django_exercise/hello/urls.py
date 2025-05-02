from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("it3witch", views.it3witch, name="it3witch"),
    path("roxy", views.roxy, name="roxy"),
    path("<str:name>", views.greet, name="greet")
]