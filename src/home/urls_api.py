
from django.urls import path
from .views_api import *

urlpatterns = [
    path('login/', Login_view),
    path('register/', Register_view),
]