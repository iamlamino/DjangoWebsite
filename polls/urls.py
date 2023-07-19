from django.urls import path

from . import views
from rest_framework import routers
from polls.views import UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
urlpatterns = [
    path("",views.index, name="index"),
    path("authentificated/", views.authentificated, name="authentificated"),
    path("edit/<int:user_id>/",views.edit,name="edit"),
    path("remove/<int:user_id>/",views.remove,name="remove"),
    
    


]
