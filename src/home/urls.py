
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('login/', login_view, name = "login_view"),
    path('register/', register_view, name = "register_view"),
    path('addblog/',add_blog_view, name = "add_blog_view"),
    # path('seeblog/',see_blog_view, name = "see_blog_view"),
    path('blogdetail/<slug>',blog_detail_view, name = "blog_detail_view"),
    path('seeblog/',see_blog_view, name = "see_blog_view"),
    path('delete/<slug>',delete_view, name = "delete_view"),
    path('updateblog/<slug>',blog_update, name = "blog_update"),
    path('logout/',logout_view, name = "logout_view"),
    path('verify/<token>/',verify, name = "verify"),

]

