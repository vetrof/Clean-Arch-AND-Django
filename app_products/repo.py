from app_products.models import Product

# Обращаемся к данным. Не обращаемся к другим репозиториям - только через сервисы.
class ProductRepo:
    def get_by_id(self, id):
        result = Product.objects.filter(id=id).first()
        return result

