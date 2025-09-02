from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app_products.repo import ProductRepo
from app_products.service import ProductService


# В хендлере - принимаем данные, парсим, сериализуем, формируем выходные структуры и ошибки.
class ProductCrud(APIView):

    # Инжектим зависимости
    repo = ProductRepo()
    service = ProductService(repo)

    def get(self, request, id):
        result, discount = self.service.get_product(id)
        if result:
            return Response({"product": result})
        else:
            return Response({"product": result}, status=status.HTTP_404_NOT_FOUND)

