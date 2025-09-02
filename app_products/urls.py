from django.contrib import admin
from django.urls import path, include

from app_products.views import ProductCrud

urlpatterns = [
    path('get/<int:id>', ProductCrud.as_view()),
]