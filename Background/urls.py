from django.urls import path
from .views import landing,upload, signup, login_view,logout_view 

urlpatterns = [ path("", landing),
                path("upload", upload),
                path("signup", signup ),
                path("login", login_view),
                path("signup", signup),
                path("login_view", login_view),
                path("logout", logout_view )]
