from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("authentificated/", views.authentificated, name="authentificated"),
    path("edit/<int:user_id>/",views.edit,name="edit"),
    path("remove/<int:user_id>/",views.remove,name="remove"),
    path("update/<int:user_id>/",views.update,name="update"),

]