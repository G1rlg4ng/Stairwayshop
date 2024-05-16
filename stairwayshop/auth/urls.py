from django.urls import path
from . import views as myviews


urlpatterns = [
    path("register/", myviews.register, name='registration-url'),
    path("login/", myviews.signin, name='login'),
    path("logout/", myviews.signout, name='logout'),
]
