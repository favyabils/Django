from django.urls import path
from .views import landing,upload

urlpatterns = [
    path("", landing),
    path("upload", upload),
]