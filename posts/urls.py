from django.conf.urls import url
from django.urls import path

from . import views

app_name="posts"

urlpatterns =[
url(r"^$",views.index, name = "index"),
path("about/",views.about,name="about"),
path("home/",views.about,name="home"),
]
