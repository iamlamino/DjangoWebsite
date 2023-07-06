from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lamine", views.lamine, name="lamine"),
]