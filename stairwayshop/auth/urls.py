from django.urls import path
from . import views as myviews

urlpatterns = [
    path("register/", myviews.register, name='registration-url'),
]
