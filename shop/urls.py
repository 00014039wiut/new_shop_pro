from django.contrib import admin
from django.urls import path

from shop.views import product_list, detail

urlpatterns = [
    path('home/', product_list, name='home'),
    path("product-detail/<int:product_id>", detail, name="detail"),
]