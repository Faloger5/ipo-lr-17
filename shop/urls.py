from django.urls import path
from shop import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("shop/", views.shop, name="shop"),
]

