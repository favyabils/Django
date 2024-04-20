from django.urls import path
from .views import landing,upload,login,signup

urlpatterns = [
    path("", landing),
    path("upload", upload),
    path("signup", signup ),
    path("login", login)
]